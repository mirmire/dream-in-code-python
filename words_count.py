#!/usr/bin/python3
# This program counts the number of words in a given sentence.
words = []
counted_words = []


def count_words(string):
    for word in string.split():
        words.append(word)

    print("\nThe given string has {} words.\n".format(len(words)))
    print("STRINGS".center(15), "OCCURENCES")
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
    print("\nWith this program, you can count number of words and occurences\n"
          "of each word in user specified file.\n")
    main()
