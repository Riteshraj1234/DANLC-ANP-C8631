# Q 2. Write a Python program that prompts the user to input an integer and raises
# (use custom exception to raise this error:it will be raised if the value provided is not between 1 to 1000)
# a ValueError exception if the input is not a valid integer.

class ValueOutOfRangeError(Exception):
    def __init__(self, message="Input value is not between 1 and 1000"):
        self.message = message
        super().__init__(self.message)

def main():
    while True:
        try:
            user_input = input("Please enter an integer between 1 and 1000: ")
            number = int(user_input)
            if number < 1 or number > 1000:
                raise ValueOutOfRangeError
            break  # Break the loop if input is valid
        except ValueError:
            print("Error: Please enter a valid integer.")
        except ValueOutOfRangeError as e:
            print(f"Error: {e}")

    print(f"Valid input: {number}")

if __name__ == "__main__":
    main()




