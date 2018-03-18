#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("string", help="the string to be reversed")
args = parser.parse_args()

print(args.string[::-1])
