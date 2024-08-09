# Write a function display_words() in python to read
# lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    filename = input("Write your file location: ")
    with open(filename, "r") as file:
        wordlist = file.read().split()
        count = 0
        for i in wordlist:
            if len(i) > 4:
                print(i)
                count += 1
        return count

if __name__ == '__main__':
    print(display_words())
# display_words()