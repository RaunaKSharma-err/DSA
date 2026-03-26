# Minimum Bit Flips to Convert Number.
start = 10
goal = 7
n = start ^ goal
count = 0
for i in range(0, 32):
    if n & (1 << i) != 0:
        count += 1
print(count)
