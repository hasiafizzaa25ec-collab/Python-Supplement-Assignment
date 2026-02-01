# Problem 81: Check if string has balanced brackets
# Find and fix the error
def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:           # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0  # True if all brackets matched

expr = "{[()]}"
print("Balanced:", balanced_brackets(expr))

