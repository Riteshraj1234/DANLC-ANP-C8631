"""
Q3. Wap to input  10 numbers from user and find their sum and average.
"""
sum = 0
for i in range(1,11):
    num = int(input("Enter ten number: "))
    sum += num
avg = sum / 10
print(f"sum is: {sum} \t Average is:{avg}" )