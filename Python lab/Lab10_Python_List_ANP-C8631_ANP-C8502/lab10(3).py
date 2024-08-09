#3. Write a Python program to find duplicate values from a list and display those.
def find_duplicates(input_list):

    frequency_dict = {}

    duplicates = []

    for item in input_list:
        if item in frequency_dict:

            if frequency_dict[item] == 1:
                duplicates.append(item)
            frequency_dict[item] += 1
        else:

            frequency_dict[item] = 1

    return duplicates

if __name__ == "__main__":

    my_list = [1, 2, 3, 2, 4, 5, 6, 1, 3, 7, 8, 8, 9]
    duplicate_values = find_duplicates(my_list)


    if duplicate_values:
        print("Duplicate values found in the list:")
        print(duplicate_values)
    else:
        print("No duplicate values found in the list.")
