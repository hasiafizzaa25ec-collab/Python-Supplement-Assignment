# Problem 77: Check if number is perfect square
# Find and fix the error
def is_perfect_square(n):
    if n < 0:
        return False  # Negative numbers cannot be perfect squares

    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

print("Is 16 perfect square?", is_perfect_square(16))
print("Is 15 perfect square?", is_perfect_square(15))

