#2.	Wap to check whether a number is negative, positive or zero.

x = int(input("Enter Any Number : "))
if x < 0:
    print(f"{x} is Negative Number")
elif x > 0:
    print(f"{x} is Positive Number")
else:
    print(F"{x} is Zero")