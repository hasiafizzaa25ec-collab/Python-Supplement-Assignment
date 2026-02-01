# Problem 91: Implement selection sort
# Find and fix the error

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find index of minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

numbers = [64, 25, 12, 22, 11]
print("Sorted:", selection_sort(numbers))

