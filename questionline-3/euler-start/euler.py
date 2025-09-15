total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Sum using loop:", total)

a, b = 1, 2
total = 0

while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print("Sum of even Fibonacci numbers <= 4,000,000:", total)