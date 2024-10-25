# 3. Write a Python program that opens a file and handles a FileNotFoundError exception
# if the file does not exist.
def main():
    file_name = input("Enter the name of the file to open: ")

    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
