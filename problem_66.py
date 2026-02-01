# Problem 66: Find intersection of two lists
# Find and fix the error
def intersection(list1, list2):
    set2 = set(list2)  # Convert list2 to set for faster lookup
    result = [item for item in list1 if item in set2]
    return result

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print("Intersection:", intersection(l1, l2))

