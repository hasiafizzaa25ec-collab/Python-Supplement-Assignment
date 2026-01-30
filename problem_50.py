# Problem 50: Convert string to uppercase
# Find and fix the error

text = "python programming"
uppercase = ""

for char in text:
    if 'a' <= char <= 'z':          # check if character is lowercase
        uppercase += chr(ord(char) - 32)  # convert to uppercase
    else:
        uppercase += char           # keep other characters as is

print(f"Uppercase: {uppercase}")

