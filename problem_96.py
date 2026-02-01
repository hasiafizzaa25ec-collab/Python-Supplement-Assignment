# Problem 96: Find two numbers that sum to target
# Find and fix the error
def two_sum(nums, target):
    seen = {}  # Stores number -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # No solution found

numbers = [2, 7, 11, 15]
print("Indices:", two_sum(numbers, 9))

