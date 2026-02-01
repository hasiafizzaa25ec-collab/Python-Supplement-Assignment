# Problem 97: Remove element from list
# Find and fix the error
def remove_element(nums, val):
    i = 0  # Position to place next non-val element
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i  # New length of the modified list

numbers = [3, 2, 2, 3, 4, 5]
length = remove_element(numbers, 3)
print("New length:", length)
print("Modified list:", numbers[:length])

