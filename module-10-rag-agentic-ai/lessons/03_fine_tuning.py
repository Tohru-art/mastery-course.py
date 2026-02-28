"""
LESSON 3: Fine-Tuning Pre-trained Models
==========================================
Fine-tuning = taking an already-trained model and adapting it to your task.
Much faster and cheaper than training from scratch.

CodePath AI110: "fine-tuning" is an explicit learning goal.
"""

# ══════════════════════════════════════════════════════
# WHAT IS FINE-TUNING?
# ══════════════════════════════════════════════════════
"""
Pre-trained model (e.g., BERT, GPT, ResNet):
  - Trained on massive data (billions of tokens / millions of images)
  - Has learned general features (grammar, visual patterns)

Fine-tuning:
  - Take the pre-trained model
  - Train it further on YOUR smaller, task-specific dataset
  - The model adapts its knowledge to your task

WHY IT WORKS:
  Pre-training teaches general knowledge.
  Fine-tuning focuses that knowledge.

WHEN TO FINE-TUNE vs PROMPT:
  Prompt engineering: quick, no training data needed, less consistent
  Fine-tuning: better consistency, better accuracy, needs 100-10K examples
"""

# ══════════════════════════════════════════════════════
# OPTION 1: FINE-TUNING WITH HUGGING FACE
# ══════════════════════════════════════════════════════
"""
Install: pip install transformers datasets

from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer
)
from datasets import Dataset
import torch

# 1. Load pre-trained model
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 2. Prepare your dataset
data = [
    {"text": "This code is clean and efficient", "label": 1},  # good code
    {"text": "This has a bug: missing error handling", "label": 0},  # bad
    # ... more examples
]
dataset = Dataset.from_list(data)

def tokenize(examples):
    return tokenizer(examples["text"], truncation=True, padding=True, max_length=128)

tokenized = dataset.map(tokenize, batched=True)
train_ds, eval_ds = tokenized.train_test_split(test_size=0.2).values()

# 3. Fine-tune
training_args = TrainingArguments(
    output_dir="./my_model",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,         # small LR for fine-tuning
    warmup_steps=100,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
)

trainer.train()
trainer.save_model("./my_finetuned_model")

# 4. Use the fine-tuned model
from transformers import pipeline
classifier = pipeline("text-classification", model="./my_finetuned_model")
result = classifier("This function has no error handling")
print(result)  # [{'label': 'LABEL_0', 'score': 0.92}]
"""

# ══════════════════════════════════════════════════════
# OPTION 2: LoRA — Low-Rank Adaptation (Parameter-Efficient)
# ══════════════════════════════════════════════════════
"""
LoRA fine-tunes ONLY a tiny fraction of parameters (< 1%).
Used for fine-tuning large LLMs (LLaMA, Mistral, etc.) on consumer GPUs.

Install: pip install peft

from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=8,                    # rank of the low-rank matrices
    lora_alpha=32,          # scaling factor
    lora_dropout=0.1,
    target_modules=["q_lin", "v_lin"]  # which layers to adapt
)

peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()
# trainable params: 294,912 || all params: 66,955,010 || trainable%: 0.44%
# Only 0.44% of parameters are updated! Much faster and cheaper.
"""

# ══════════════════════════════════════════════════════
# OPTION 3: LLM API Fine-Tuning (Easiest)
# ══════════════════════════════════════════════════════
"""
OpenAI and Anthropic offer fine-tuning via API — no GPU needed.

Format your data as JSONL:
{"messages": [
    {"role": "system", "content": "You are a code reviewer."},
    {"role": "user", "content": "Review this: def add(x,y): return x+y"},
    {"role": "assistant", "content": "Missing type hints and docstring."}
]}

Upload and train:
  client.fine_tuning.jobs.create(
      training_file="file-xxx",
      model="gpt-4o-mini-2024-07-18",
  )

Then use your fine-tuned model by its ID.
"""

# ══════════════════════════════════════════════════════
# WHEN FINE-TUNING IS OVERKILL
# ══════════════════════════════════════════════════════
"""
Before fine-tuning, try these in order (cheaper → expensive):

1. Better prompt engineering (few-shot examples)
2. RAG (give the model your knowledge at inference time)
3. Fine-tuning on a small model
4. Fine-tuning on a large model

Fine-tuning is worth it when:
- You need consistent output format
- You have 100+ high-quality examples
- Prompt engineering doesn't give consistent results
- Latency matters (fine-tuned models are faster than few-shot)
"""

print("Lesson 3 complete — fine-tuning concepts covered.")
print("\nDone! Move on to 04_guardrails.py")
