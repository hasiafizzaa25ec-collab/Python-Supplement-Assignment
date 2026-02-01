# Problem 82: Remove adjacent duplicates
# Find and fix the error
def remove_adjacent_duplicates(text):
    result = []

    for char in text:
        if not result or result[-1] != char:  # Add if different from last
            result.append(char)

    return "".join(result)

s = "programming"
print("After removal:", remove_adjacent_duplicates(s))

