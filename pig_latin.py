#!/usr/bin/python3
"""Pig latin game script"""


def play():
    vowels = "aeiou"
    suffix = "ay"
    index = 0
    word = input("What to change to Pig latin form?: ")
    for vowel in word:
        if word[0] in vowels:
            print(word + suffix)
            break
        elif word[index] in vowels:
            pig_latin = word[index:] + word[:index]
            print("Here we go: {}".format(pig_latin + suffix))
            break
        else:
            index += 1


if __name__ == "__main__":
    print("This is a Pig Latin game. The word you give will be altered\n"
          "in some interesting way. Try it!\n")
    play()
