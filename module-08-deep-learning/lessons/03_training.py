"""
LESSON 3: Training a Neural Net with PyTorch
==============================================
The complete training loop used in every PyTorch project.
This pattern is used in GPT, ResNet, and every other model.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

torch.manual_seed(42)

# ══════════════════════════════════════════════════════
# 1. DEFINE THE MODEL
# ══════════════════════════════════════════════════════
class MLP(nn.Module):
    """Multi-Layer Perceptron classifier."""

    def __init__(self, input_dim, hidden_dim, output_dim, dropout=0.3):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, output_dim)
        )

    def forward(self, x):
        return self.network(x)


model = MLP(input_dim=20, hidden_dim=64, output_dim=2)
print("Model architecture:")
print(model)
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"\nTotal parameters: {total_params:,}")
print(f"Trainable parameters: {trainable_params:,}")

# ══════════════════════════════════════════════════════
# 2. PREPARE DATA
# ══════════════════════════════════════════════════════
# Simulate a classification dataset
np.random.seed(42)
X = np.random.randn(1000, 20).astype(np.float32)
y = (X[:, 0] + X[:, 1] > 0).astype(np.int64)

# Convert to PyTorch tensors
X_tensor = torch.tensor(X)
y_tensor = torch.tensor(y)

# Train/val split
split = int(0.8 * len(X))
train_dataset = TensorDataset(X_tensor[:split], y_tensor[:split])
val_dataset   = TensorDataset(X_tensor[split:], y_tensor[split:])

# DataLoader: batches + shuffling
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader   = DataLoader(val_dataset,   batch_size=64, shuffle=False)

print(f"\nTrain batches: {len(train_loader)}, Val batches: {len(val_loader)}")

# ══════════════════════════════════════════════════════
# 3. TRAINING LOOP
# ══════════════════════════════════════════════════════
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.5)

history = {"train_loss": [], "val_loss": [], "val_acc": []}

for epoch in range(30):
    # ── TRAIN ──────────────────────────────────────────
    model.train()   # important! enables dropout
    train_loss = 0.0
    for X_batch, y_batch in train_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)

        optimizer.zero_grad()           # clear old gradients
        outputs = model(X_batch)        # forward pass
        loss = criterion(outputs, y_batch)  # compute loss
        loss.backward()                 # backpropagation
        optimizer.step()                # update weights

        train_loss += loss.item()
    train_loss /= len(train_loader)

    # ── VALIDATE ───────────────────────────────────────
    model.eval()    # important! disables dropout
    val_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():   # no gradients needed for eval
        for X_batch, y_batch in val_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            outputs = model(X_batch)
            val_loss += criterion(outputs, y_batch).item()
            preds = outputs.argmax(dim=1)
            correct += (preds == y_batch).sum().item()
            total += len(y_batch)

    val_loss /= len(val_loader)
    val_acc = correct / total
    scheduler.step()

    history["train_loss"].append(train_loss)
    history["val_loss"].append(val_loss)
    history["val_acc"].append(val_acc)

    if (epoch + 1) % 5 == 0:
        lr = optimizer.param_groups[0]["lr"]
        print(f"Epoch {epoch+1:2d}: train={train_loss:.4f}, val={val_loss:.4f}, acc={val_acc:.3f}, lr={lr:.6f}")

print(f"\nBest val accuracy: {max(history['val_acc']):.3f}")

# ══════════════════════════════════════════════════════
# 4. SAVE & LOAD MODEL
# ══════════════════════════════════════════════════════
# Save
torch.save(model.state_dict(), "model_weights.pt")
print("\nModel saved!")

# Load
model_loaded = MLP(input_dim=20, hidden_dim=64, output_dim=2)
model_loaded.load_state_dict(torch.load("model_weights.pt"))
model_loaded.eval()
print("Model loaded successfully!")

import os
os.remove("model_weights.pt")

# ── THE TRAINING LOOP — memorize this pattern ─────────────────────────────────
"""
for epoch in range(num_epochs):
    # TRAIN
    model.train()
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()

    # VALIDATE
    model.eval()
    with torch.no_grad():
        for X_batch, y_batch in val_loader:
            outputs = model(X_batch)
            ...
"""

print("\nDone! Move on to 04_llm_apis.py")
