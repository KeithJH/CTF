# file-run1
## Description
- **Tags**:
    - picoCTF 2022
    - Reverse Engineering
- **Author**: Will Hong

A program has been provided to you, what happens if you try to run it on the command line?

Download the program [here](https://artifacts.picoctf.net/c/309/run).

## Exploration

We can simply pull down the executable and mark it with execute permissions and it will output the flag.

```
$ wget https://artifacts.picoctf.net/c/309/run
$ chmod +x run
$./ run
picoCTF{REDACTED}
```

Or, we could also just search the strings of the file
```
$ strings run | grep picoCTF
picoCTF{REDACTED}
```