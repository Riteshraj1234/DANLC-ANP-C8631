"""
6. Given the nested list `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, write code to print the second element of the first list and the third element of the third list.
1 2 3
4 5 6
7 8 9
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])
print(matrix[2][2])
for r in range (0,3):
    for c in range (0,3):
        print(matrix[r][c],end="\t")
        print()
for r in range (0,3):
    for c in range (0,3):
        print(matrix[c][r],end="\t")
        print()