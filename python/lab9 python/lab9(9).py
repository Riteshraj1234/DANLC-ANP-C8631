"""
9. Exception Handling with Logging
   - Write a function `read_and_log` that reads a file and logs any exceptions that occur to a separate log file. Use exception handling to manage:
    - File not found.
     - Permission denied.
     - Any other error.
   - Ensure the function writes detailed error messages to the log file and test it with various scenarios.
"""
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_log(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            # Process the content as needed
            print(f"File content:\n{content}")
    except FileNotFoundError as e:
        logging.error(f"File not found error: {e}")
        print(f"Error: File '{file_name}' not found.")
    except PermissionError as e:
        logging.error(f"Permission denied error: {e}")
        print(f"Error: Permission denied while trying to access file '{file_name}'.")
    except Exception as e:
        logging.error(f"Error reading file '{file_name}': {e}")
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the file to read: ")
    read_and_log(file_name)
