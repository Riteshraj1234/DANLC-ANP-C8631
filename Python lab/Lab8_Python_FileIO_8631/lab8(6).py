# Wap to search a particular word in a file and also prints number of occurrences.

def search_wprd_in_file(filename, word):
    with open(filename,"r") as file:
        text = file.read()
        word_count = text.lower().split().count(word.lower())
        print(f"The word {word} occurs {word_count} times in a file {filename}")

filename = input('Enter the file name with path: ')
word = input('Enter the word to search: ')
search_wprd_in_file(filename, word)