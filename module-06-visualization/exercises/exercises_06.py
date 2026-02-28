"""
MODULE 6 EXERCISES — Data Visualization
=========================================
Run: python exercises/exercises_06.py
Install: pip install matplotlib seaborn
"""
import matplotlib.pyplot as plt
import numpy as np

# ══════════════════════════════════════════════════════
# EXERCISE 1: Training Curve
# ══════════════════════════════════════════════════════
def plot_training_history(train_losses, val_losses, train_accs, val_accs, save_path=None):
    """
    Create a 2-subplot figure:
    Left: train vs val loss over epochs
    Right: train vs val accuracy over epochs

    Both plots should have:
    - Labeled axes (Epoch, Loss / Accuracy)
    - A legend
    - A title
    - Grid lines

    If save_path is given, save the figure there.
    """
    # YOUR CODE HERE
    pass

# ══════════════════════════════════════════════════════
# EXERCISE 2: Confusion Matrix Heatmap
# ══════════════════════════════════════════════════════
def plot_confusion_matrix(cm, class_names, save_path=None):
    """
    Plot a confusion matrix as a heatmap.
    - Color cells by value (lighter = lower)
    - Show number in each cell
    - Label x-axis "Predicted", y-axis "Actual"
    - Show class_names as tick labels

    cm: 2D numpy array
    class_names: list of strings
    """
    # YOUR CODE HERE
    pass

# ══════════════════════════════════════════════════════
# EXERCISE 3: Model Comparison Bar Chart
# ══════════════════════════════════════════════════════
def plot_model_comparison(model_names, accuracies, save_path=None):
    """
    Bar chart comparing model accuracies.
    - Bars should be sorted from highest to lowest
    - Color the best model green, others blue
    - Show the accuracy value on top of each bar
    - Add a horizontal red dashed line at 90% threshold
    - Title: "Model Accuracy Comparison"
    """
    # YOUR CODE HERE
    pass

# ══════════════════════════════════════════════════════
# TEST RUNNER
# ══════════════════════════════════════════════════════
def run_tests():
    print("=== MODULE 6 TESTS ===")
    print("Visualization tests are manual — run the functions and check the plots.\n")

    # Test 1
    np.random.seed(42)
    epochs = 20
    t_loss = [1/(i+1) + np.random.normal(0, 0.02) for i in range(epochs)]
    v_loss = [1.1/(i+1) + np.random.normal(0, 0.03) for i in range(epochs)]
    t_acc  = [1 - 0.9/(i+2) + np.random.normal(0, 0.01) for i in range(epochs)]
    v_acc  = [1 - 0.95/(i+2) + np.random.normal(0, 0.015) for i in range(epochs)]
    plot_training_history(t_loss, v_loss, t_acc, v_acc, save_path="training_history.png")
    print("  Test 1: training_history.png created" if __import__("os").path.exists("training_history.png") else "  Test 1: MISSING training_history.png")

    # Test 2
    cm = np.array([[45,5,0],[3,38,9],[1,4,45]])
    plot_confusion_matrix(cm, ["Cat","Dog","Bird"], save_path="confusion_matrix.png")
    print("  Test 2: confusion_matrix.png created" if __import__("os").path.exists("confusion_matrix.png") else "  Test 2: MISSING confusion_matrix.png")

    # Test 3
    models = ["Logistic Reg","Random Forest","SVM","Neural Net"]
    accs = [0.82, 0.91, 0.88, 0.94]
    plot_model_comparison(models, accs, save_path="model_comparison.png")
    print("  Test 3: model_comparison.png created" if __import__("os").path.exists("model_comparison.png") else "  Test 3: MISSING model_comparison.png")

    print("\nOpen the PNG files to visually verify your plots.")
    print("Commit when all 3 plots look correct.")

if __name__ == "__main__":
    run_tests()
