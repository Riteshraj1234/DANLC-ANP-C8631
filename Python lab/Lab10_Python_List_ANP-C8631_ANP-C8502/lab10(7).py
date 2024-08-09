"""Write a function `transpose(matrix)` that takes a matrix (list of lists) and returns its transpose.
"""
a = [[10, 20], [11, 22], [33, 44], [55, 66]]

# original list
print("Original List :-")
for r in range(0, len(a)):
    for c in range(0, len(a[r])):
        print(a[r][c], end="\t")
    print()
# Print this list in Transpose
print("Print this list in Transpose")

for c in range(0, 2):
    for r in range(0, len(a)):
        print(a[r][c], end="\t")
    print()

# creating a new list

# 00 01
#  1  2
# 10 11
#  3  4
# 20 21
#  5  6
# 30 31
#  7  8
# Transpose
# 00 01 02 03
#  1  2  3  4
# 10 11 12 13
#  5  6  7  8
# b[0][0] = a[0][0]
# b[0][1] = a[1][0]
# b[0][2] = a[2][0]
# b[0][3] = a[3][0]
#
# b[1][0] = a[0][1]
# b[1][1] = a[1][1]
# b[1][2] = a[2][1]
# b[1][3] = a[3][1]
b = []

for r in range(0, 2):
    cols =[]
    for c in range(0, 4):
        # b[r][c] = a[c][r]
        cols.append(a[c][r])
    b.append(cols)
print("New Transposed list")
for r in range(0, len(b)):
    for c in range(0, len(b[r])):
        print(b[r][c], end="\t")
    print()
a = b

# Q9
x = [1,2,3,4]
y = [11,22,33,44]

mergelist = x+y
print(mergelist)

# run the loop of rows until we reach the last element

temp = []
i = 0
for r in range(0, len(mergelist)):
    t=[]
    for c in range(0, 2):
        t.append(mergelist[i])
        i += 1
        print(i)

    temp.append(mergelist)
    if i == len(mergelist):
        break

print("New Merged list")
for r in range(0, len(temp)):
    for c in range(0, len(temp[r])):
        print(temp[r][c], end="\t")
    print()