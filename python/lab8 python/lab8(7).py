# Wap to search a string and replace it with another string (all occurrences).

def search_and_replace_in_file(filename, search_string, replace_string):
    with open(filename, "r") as file:
        content = file.read()

    new_content = content.replace(search_string, replace_string)

    with open(filename, 'w') as file:
        file.write(new_content)

    print(f'All occurrences of "{search_string}" have been replaced with "{replace_string}" in the file {filename}.')

filename = input('Enter the file name with path: ')
search_string = input('Enter the string to search: ')
replace_string = input('Enter the string to replace with: ')

search_and_replace_in_file(filename, search_string, replace_string)