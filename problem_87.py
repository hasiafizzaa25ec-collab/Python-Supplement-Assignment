# Problem 87: Generate Pascal's triangle
# Find and fix the error

def pascals_triangle(n):
    triangle = []

    for i in range(n):
        # Initialize row with 1's
        row = [1] * (i + 1)

        # Fill inner elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

# Generate 5 rows
triangle = pascals_triangle(5)
for row in triangle:
    print(row)

