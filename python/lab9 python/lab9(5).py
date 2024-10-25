# 5. File Parsing with Detailed Error Handling
# #    - Write a function `parse_file` that reads a file
# containing numerical data (one number per line)
# and returns a list of these numbers. Use exception handling to
# manage:
# #      - File not found.
# #      - Permission denied.
# #      - Value errors (e.g., non-numeric data).
# #    - Provide detailed error messages indicating the line number and nature of the error.

def parse_file(filename):
    num_list = []

    try:
        file = open(filename, "r")

        for line in file:
            # a = int(line)
            # num_list.append(a)
            num_list.append(int(line))
        print("List Values : ",num_list)

        file.close()
    except FileNotFoundError as fe:
        print("Exception 1 : ",fe)
    except PermissionError as pe:
        print("Exception 2 : ", pe)
    except ValueError as ve:
        print("Exception 3 : ",ve)


parse_file(input("Enter File Name : "))