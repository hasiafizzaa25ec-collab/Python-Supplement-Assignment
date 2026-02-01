# Problem 94: Count bits set to 1
# Find and fix the error
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Add 1 if the last bit is set
        n = n >> 1      # Shift right by 1
    return count

print("Set bits in 15:", count_set_bits(15))

