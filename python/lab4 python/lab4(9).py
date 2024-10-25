"""
wap to print all the leap years from 1 to n
"""
n =45
int(input("Enter number: "))
for i in range(1 , n+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i, " ", end="")

