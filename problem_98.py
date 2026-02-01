# Problem 98: Check if power of two
# Find and fix the error
def is_power_of_two(n):
    if n <= 0:
        return False
    # A number is a power of two if it has exactly one set bit
    return (n & (n - 1)) == 0

print("Is 16 power of 2?", is_power_of_two(16))
print("Is 18 power of 2?", is_power_of_two(18))

