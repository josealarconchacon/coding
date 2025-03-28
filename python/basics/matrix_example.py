import numpy as np

# creating a matrix using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])      # First row: [1, 2, 3]
print(matrix[1][2])   # Second row, third element: 6

# loop through a matrix
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()  # New line after each row

# modifying matrix elements
matrix[0][1] = 99
print(matrix[0])  # [1, 99, 3]

# adding rows or columns manually
matrix.append([10, 11, 12]) # Add a row
for row in matrix: # Add a column (to each row)
    row.append(0)
print(matrix)

# matrix operations with numPy 
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# Matrix addition
print(a + b)
# Matrix multiplication
print(np.dot(a, b))
# Transpose
print(a.T)
# Accessing elements
print(a[1, 1])  # 4
