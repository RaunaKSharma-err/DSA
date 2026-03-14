import numpy as np

# Initialize weights and bias
w1 = 0
w2 = 0
b = 0

# Training data for AND gate (Bipolar representation)
inputs = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

targets = [1, -1, -1, -1]

# Hebbian Learning Rule
for (x1, x2), t in zip(inputs, targets):
    w1 = w1 + x1 * t
    w2 = w2 + x2 * t
    b = b + t

# Display learned weights
print("Learned Weights and Bias")
print("w1 =", w1)
print("w2 =", w2)
print("b  =", b)


# Hebbian Network Function
def hebb_and(x1, x2):
    net = w1 * x1 + w2 * x2 + b
    return np.sign(net)


# Testing the network
test_data = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

print("\nTesting Hebbian AND Gate")

for x1, x2 in test_data:
    result = hebb_and(x1, x2)
    print("Input:", (x1, x2), "Output:", int(result))