#!/usr/bin/python3
# A simple palindrome checker script

text = input("The string to be checked if it's a palindrome:  ")
if text == text[::-1]:
    print("{} is a palindrome.".format(text))
else:
    print("{} is not a palindrome.".format(text))
