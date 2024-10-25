"""
Q8. Wap to input 10 numbers from user and find the minimum and maximum number.
"""
max_number = float('-inf')
min_number = float('inf')

# Input 10 numbers from user
print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")
