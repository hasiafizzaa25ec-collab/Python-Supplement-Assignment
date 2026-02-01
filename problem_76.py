# Problem 76: Calculate string similarity (common characters)
# Find and fix the error
def string_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common = set1 & set2  # Intersection of sets
    return len(common)

s1 = "hello"
s2 = "world"
print("Common characters:", string_similarity(s1, s2))

