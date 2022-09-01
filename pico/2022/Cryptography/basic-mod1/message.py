#!/usr/bin/env python3
import string

mapping = string.ascii_uppercase + string.digits + "_"

with open("message.txt", "r") as message:
	chars = [mapping[int(x) % 37] for x in message.read().split()]

joined = "".join(chars)
print(f"picoCTF{{{joined}}}")
