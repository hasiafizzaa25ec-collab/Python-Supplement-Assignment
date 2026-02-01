# Problem 74: Find first non-repeating character
# Find and fix the error
def first_non_repeating(text):
    char_count = {}

    # Count occurrences of each character
def first_non_repeating(text):
    char_count = {}

def first_non_repeating(text):
    char_count = {}

    # Count occurrences of each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first character with count 1
    for char in text:
        if char_count[char] == 1:
            return char

    return None  # Return None if all characters repeat

word = "programming"
print("First non-repeating:", first_non_repeating(word))


