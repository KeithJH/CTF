# basic-mod1
## Description
- **Tags**:
    - picoCTF 2022
    - Cryptography
- **Author**: Will Hong


We found this weird message being passed around on the servers, we think we have a working decryption scheme.

Download the message [here](https://artifacts.picoctf.net/c/395/message.txt).

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)


## Exploration

Problem statement is pretty straight forward, giving a transformation function from input to output.

Taking a look at the input format we see that the file containes space seperated numbers like:
```bash
$ cat message.txt
91 322 57 124 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102
```

To form the decrypted message we then need to:
- Read content in from file
- Split on space seperator
- Convert to actual numeric values
- Take the result mod 37
- Use that value as an index into a lookup table
- Wrap the message in the flag format

```
$ ./message.py
picoCTF{REDACTED}
```