#!/usr/bin/python3
string = input("Enter a string to reverse: ")
print("String '{string}' in reverse is '{this}'.".format(string=string,
                                                         this=string[::-1]))
