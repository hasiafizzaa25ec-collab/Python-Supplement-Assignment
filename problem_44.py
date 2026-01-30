# Problem 44: Print Fibonacci sequence
# Find and fix the error
def fibonacci(n):
    fib = [0, 1]              # start with first two Fibonacci numbers
    for i in range(2, n):     # loop from 2 to n-1
        fib.append(fib[i-1] + fib[i-2])  # add previous two numbers
    return fib

print(f"First 10 Fibonacci numbers: {fibonacci(10)}")

