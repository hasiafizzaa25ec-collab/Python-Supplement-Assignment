# Problem 54: Find nth Fibonacci number
# Find and fix the error
def nth_fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

print(f"10th Fibonacci number: {nth_fibonacci(10)}")

