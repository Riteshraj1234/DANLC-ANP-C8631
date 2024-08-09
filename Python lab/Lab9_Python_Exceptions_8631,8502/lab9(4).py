"""
 4. Write a Python program that prompts the user to input two numbers and raises a
 TypeError exception if the inputs are not numerical
"""

def main():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        num1 = float(num1)
        num2 = float(num2)
        print(f"Sum of {num1} and {num2} is: {num1 + num2}")
    except ValueError:
        print("Error: Please enter numerical values.")
    except TypeError:
        print("Error: One or both inputs are not numerical.")
if __name__ == "__main__":
    main()
