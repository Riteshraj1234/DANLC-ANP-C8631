"""
write a Python program to calculate the sum of the number in a given a tuple .
"""
tuples_list = [(1, 2), (3, 4), (5, 6)]
add = 0
for i in tuples_list:
    add += sum(i)
print(f"Sum of values in the tuples : {add}")