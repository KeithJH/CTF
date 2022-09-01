# basic-mod2
## Description
- **Tags**:
    - picoCTF 2022
    - Binary Exploitation
- **Author**: Will Hong


A new modular challenge!

Download the message [here](https://artifacts.picoctf.net/c/500/message.txt).

Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Exploration
Problem statement is pretty straight forward and similar to basic-mod1, giving a transformation function from input to output. The biggest difference is the introduction of the modular inverse in the tranformation function; however, this can still be easily done in code.

Taking a look at the input format we see that the file containes space seperated numbers like:
```bash
$ cat message.txt
104 85 69 354 344 50 149 65 187 420 77 127 385 318 133 72 206 236 206 83 342 206 370
```

To form the decrypted message we then need to:
- Read content in from file
- Split on space seperator
- Convert to actual numeric values
- Find the modular inverse
- Use that value as an index into a lookup table
- Wrap the message in the flag format

Python has a built-in functionality for modular inverse that we can use
```python
>>> pow(104, -1, 41)
28
```

We can again use this as an index into a lookup table. A small catch is that the logic now starts with 1-26 as the alphabet, instead of starting at zero. We can either adjust our indexing or add a "padding" character to the beggining of the lookup table.
```python
mapping = "_" + string.ascii_uppercase + string.digits + "_"
```

Putting it all together:
```
$ ./message.py
picoCTF{REDACTED}
```