# Problem 58: Binary search implementation
# Find and fix
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1      # FIXED
        else:
            right = mid - 1     # FIXED

    return -1

