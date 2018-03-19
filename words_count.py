#!/usr/bin/python3
# This program counts the number of words in a given file 
# and prints a nice summary
words = []
counted_words = []


def count_words(string):
    for word in string.split():
        words.append(word)

    print("\nThe given file has {} words.\n".format(len(words)))
    print("STRING".center(15), "OCCURENCE")
    for each_word in words:
        if each_word not in counted_words:
            print(each_word.center(15), words.count(each_word))
            counted_words.append(each_word)


def main():
    filepath = input("Write the absolute path of the filename: ")

    try:
        with open(filepath, "r") as f:
            count_words(f.read())
    except (FileNotFoundError, IsADirectoryError):
        print("File does not exist or not a valid file name.")
        return


if __name__ == '__main__':
    print("\nSee each word's occurence in a file in a beautiful format.\n"
          "Note:  Currently it handles complex data poorly.\n")
    main()
