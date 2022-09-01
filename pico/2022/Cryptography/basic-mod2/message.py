#!/usr/bin/env python3
import string

def index(x):
	return pow(int(x), -1, 41)

mapping = "_" + string.ascii_uppercase + string.digits + "_"

with open("message.txt", "r") as message:
	chars = [mapping[index(x)] for x in message.read().split()]

joined = "".join(chars)
print(f"picoCTF{{{joined}}}")
