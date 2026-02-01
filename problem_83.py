# Problem 83: Find kth smallest element
# Find and fix the error
def kth_smallest(arr, k):
    sorted_arr = sorted(arr)
    if 1 <= k <= len(arr):
        return sorted_arr[k - 1]  # Fix indexing
    else:
        return None  # Invalid k

numbers = [7, 10, 4, 3, 20, 15]
print("3rd smallest:", kth_smallest(numbers, 3))

