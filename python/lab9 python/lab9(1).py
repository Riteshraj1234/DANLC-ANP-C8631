#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a=int(input("enter a  1st number:"))
    b=int(input("enter a  2nd number:"))
    result=a/b
except ZeroDivisionError:
    # Handle the exception here
    print("Division by zero is not allowed.")
     