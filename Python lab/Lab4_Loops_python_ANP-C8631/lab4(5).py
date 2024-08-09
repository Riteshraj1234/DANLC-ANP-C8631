"""
Q5. Wap to print the sum of the series
1  4 9 16 25 36 49 64
"""
n = 0
for i in range(1, 9):
    term = i * i
    n += term
print("sum of series 1 4 9 16 25 36 49 64 :", n)