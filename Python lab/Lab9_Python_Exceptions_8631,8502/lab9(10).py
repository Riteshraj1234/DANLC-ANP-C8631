"""
10. Write a function convert_to_float that takes a list of strings and attempts to convert each string to a float. Use exception handling to manage:
Value errors (e.g., strings that cannot be converted to float).
Any other unexpected errors.
The function should return a list of successfully converted floats and a list of errors (with the original string and the error message).
"""
def convert_to_float(str_list):
    successful_floats = []
    conversion_errors = []

    for s in str_list:
        try:
            float_value = float(s)
            successful_floats.append(float_value)
        except ValueError as e:
            conversion_errors.append((s, str(e)))
        except Exception as e:
            conversion_errors.append((s, f"Unexpected error: {str(e)}"))

    return successful_floats, conversion_errors
if __name__ == "__main__":
    strings = ["3.14", "2.718", "hello", "42", "7.5", "invalid"]
    floats, errors = convert_to_float(strings)

    print("Successfully converted floats:", floats)
    print("Conversion errors:")
    for error in errors:
        print(f"  {error[0]}: {error[1]}")
