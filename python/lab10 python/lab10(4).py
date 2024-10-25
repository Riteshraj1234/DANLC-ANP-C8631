"""
4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
Original list: [1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])
"""
def split_list(original_list, length_first_part):

    if length_first_part < 0 or length_first_part > len(original_list):
        raise ValueError("Length of the first part is out of range.")


    first_part = original_list[:length_first_part]
    second_part = original_list[length_first_part:]

    return (first_part, second_part)

if __name__ == "__main__":

    original_list = [1, 1, 2, 3, 4, 4, 5, 1]
    length_first_part = 3

    try:

        first_part, second_part = split_list(original_list, length_first_part)
        # Print the result
        print(f"Original list: {original_list}")
        print(f"Length of the first part of the list: {length_first_part}")
        print(f"Splitted the said list into two parts: ({first_part}, {second_part})")
    except ValueError as ve:
        print(f"Error: {ve}")
