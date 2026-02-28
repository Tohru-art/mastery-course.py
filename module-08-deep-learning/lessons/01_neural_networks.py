"""
LESSON 1: Neural Network Fundamentals
========================================
Before touching PyTorch, understand WHAT neural networks are doing.
This lesson builds a tiny neural net from scratch using only NumPy.
"""

import numpy as np

np.random.seed(42)

# ══════════════════════════════════════════════════════
# WHAT IS A NEURON?
# ══════════════════════════════════════════════════════
"""
A single neuron:
  1. Takes inputs: x1, x2, ..., xn
  2. Multiplies by weights: w1, w2, ..., wn
  3. Adds a bias: b
  4. Applies an activation function: output = f(w·x + b)

This is just: output = f(dot(weights, inputs) + bias)
"""

def sigmoid(x):
    """Squishes any value into [0, 1]. Classic activation."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Needed for backpropagation."""
    s = sigmoid(x)
    return s * (1 - s)

def relu(x):
    """Rectified Linear Unit — most common in modern networks."""
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

# A single neuron
def neuron(inputs, weights, bias, activation=sigmoid):
    z = np.dot(weights, inputs) + bias
    return activation(z), z

inputs = np.array([2.0, 3.0])
weights = np.array([0.5, -0.3])
bias = 0.1

output, z = neuron(inputs, weights, bias)
print(f"z = {z:.4f}, output = {output:.4f}")

# ══════════════════════════════════════════════════════
# NEURAL NETWORK FROM SCRATCH
# ══════════════════════════════════════════════════════
class SimpleNeuralNetwork:
    """
    2-layer neural net (1 hidden layer):
      Input (2) → Hidden (4) → Output (1)
    Trained with gradient descent + backpropagation.
    """

    def __init__(self, input_size=2, hidden_size=4, output_size=1, lr=0.1):
        # Initialize weights with small random values
        self.W1 = np.random.randn(hidden_size, input_size) * 0.1
        self.b1 = np.zeros((hidden_size, 1))
        self.W2 = np.random.randn(output_size, hidden_size) * 0.1
        self.b2 = np.zeros((output_size, 1))
        self.lr = lr

    def forward(self, X):
        """Forward pass: compute predictions."""
        # X shape: (input_size, n_samples)
        self.Z1 = self.W1 @ X + self.b1    # (hidden, n)
        self.A1 = relu(self.Z1)             # (hidden, n)
        self.Z2 = self.W2 @ self.A1 + self.b2  # (output, n)
        self.A2 = sigmoid(self.Z2)          # (output, n) — final prediction
        return self.A2

    def compute_loss(self, y_pred, y_true):
        """Binary cross-entropy loss."""
        m = y_true.shape[1]
        loss = -np.mean(y_true * np.log(y_pred + 1e-8) +
                        (1 - y_true) * np.log(1 - y_pred + 1e-8))
        return loss

    def backward(self, X, y_true):
        """Backpropagation: compute gradients."""
        m = X.shape[1]

        # Output layer gradients
        dZ2 = self.A2 - y_true             # (output, n)
        dW2 = (dZ2 @ self.A1.T) / m
        db2 = np.sum(dZ2, axis=1, keepdims=True) / m

        # Hidden layer gradients
        dA1 = self.W2.T @ dZ2
        dZ1 = dA1 * relu_derivative(self.Z1)
        dW1 = (dZ1 @ X.T) / m
        db1 = np.sum(dZ1, axis=1, keepdims=True) / m

        # Update weights (gradient descent)
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def train(self, X, y, epochs=1000, print_every=200):
        losses = []
        for epoch in range(epochs):
            y_pred = self.forward(X)
            loss = self.compute_loss(y_pred, y)
            self.backward(X, y)
            losses.append(loss)
            if epoch % print_every == 0:
                print(f"  Epoch {epoch:4d}: loss = {loss:.4f}")
        return losses

    def predict(self, X, threshold=0.5):
        return (self.forward(X) >= threshold).astype(int)


# ── Train on XOR problem ──────────────────────────────
# XOR: [0,0]→0, [0,1]→1, [1,0]→1, [1,1]→0
# Linear models can't solve XOR — neural nets can!
X = np.array([[0,0,1,1], [0,1,0,1]])   # shape (2, 4)
y = np.array([[0,1,1,0]])              # shape (1, 4)

print("Training on XOR:")
nn = SimpleNeuralNetwork(input_size=2, hidden_size=4, lr=0.5)
nn.train(X, y, epochs=2000, print_every=500)

print("\nXOR Predictions:")
preds = nn.predict(X)
for i in range(4):
    inp = X[:, i]
    print(f"  [{inp[0]}, {inp[1]}] → {preds[0, i]} (true: {y[0, i]})")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. A neuron = weighted sum + activation function
# 2. Forward pass: input → layers → prediction
# 3. Loss function: measures how wrong the prediction is
# 4. Backpropagation: compute gradients via chain rule
# 5. Gradient descent: update weights to reduce loss
# 6. In practice, use PyTorch — it handles all of this automatically
print("\nDone! Move on to 02_pytorch_basics.py")
