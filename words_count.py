#!/usr/bin/python3
# This program counts the number of words in a given sentence.


def main():
    words = []
    counted_words = []
    string = input("Number of words in: ")
    for word in string.split():
        words.append(word)

    print("\nThe given string has {} words.\n".format(len(words)))
    print("STRINGS".center(15), "OCCURENCES")
    for each_word in words:
        if each_word not in counted_words:
            print(each_word.center(15), words.count(each_word))
            counted_words.append(each_word)


if __name__ == '__main__':
    main()
