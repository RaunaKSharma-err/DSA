import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([5, 7, 9, 11, 13], dtype=float)

# Initialize parameters
m, b = 0.0, 0.0
learning_rate = 0.01
iterations = 10000
n = len(X)

# Gradient Descent
losses = []
lines_to_plot = []  # store some intermediate lines

for iteration in range(iterations):
    y_pred = m * X + b
    dm = (-2 / n) * np.sum(X * (y - y_pred))
    db = (-2 / n) * np.sum(y - y_pred)

    m = m - learning_rate * dm
    b = b - learning_rate * db

    loss = np.mean((y - y_pred) ** 2)
    losses.append(loss)

    # Save some lines for visualization (every 200 iterations)
    if iteration % 200 == 0:
        lines_to_plot.append((m, b))

    if iteration % 100 == 0:
        print(f"Iteration {iteration}, Loss: {loss:.4f}, m: {m:.4f}, b: {b:.4f}")

print("\nTraining completed!")
print(f"Final parameters: m = {m:.4f}, b = {b:.4f}")

# Plot the data points and regression lines
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Data Points")

# Plot intermediate lines (possible fits during training)
colors = ["orange", "purple", "cyan", "magenta", "gray"]
for i, (mi, bi) in enumerate(lines_to_plot):
    plt.plot(
        X,
        mi * X + bi,
        color=colors[i % len(colors)],
        linestyle="--",
        alpha=0.7,
        label=f"Iteration {i * 200}",
    )

# Plot final regression line
plt.plot(
    X, m * X + b, color="red", label=f"Final Line: y={m:.2f}x+{b:.2f}", linewidth=2
)

# Display final m and b on the graph
plt.text(1, max(y) + 0.5, f"Final m = {m:.2f}, b = {b:.2f}", color="red", fontsize=12)

plt.title("Linear Regression Fit with Gradient Descent")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Plot the loss curve
plt.figure(figsize=(8, 5))
plt.plot(range(iterations), losses, color="green")
plt.title("Loss Curve over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Mean Squared Error (Loss)")
plt.grid(True)
plt.show()
