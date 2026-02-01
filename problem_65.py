# Problem 65: Check if list has duplicates
# Find and fix the error
def has_duplicates(lst):
    seen = set()  # Use a set for faster lookups
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

numbers = [1, 2, 3, 4, 5]
print("Has duplicates:", has_duplicates(numbers))

