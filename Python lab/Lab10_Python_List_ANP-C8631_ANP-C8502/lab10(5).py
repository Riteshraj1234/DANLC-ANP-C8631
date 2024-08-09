"""
5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
Original list: ['red', 'green', 'white', 'black']
Traverse the said list in reverse order: black white green red
"""

def traverse_in_reverse(input_list):

    for index, element in reversed(list(enumerate(input_list))):
        print(f"Element at index {index}: {element}")

if __name__ == "__main__":
    original_list = ['red', 'green', 'white', 'black']
    print("Original list:", original_list)
    print("Traverse the said list in reverse order:")
    traverse_in_reverse(original_list)
