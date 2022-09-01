# file-run2
## Description
- **Tags**:
    - picoCTF 2022
    - Reverse Engineering
- **Author**: Will Hong

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

Download the program [here](https://artifacts.picoctf.net/c/352/run).

## Exploration

We can simply pull down the executable and mark it with execute permissions and it will output the flag. It wants an argument of "Hello!"

```
$ wget https://artifacts.picoctf.net/c/352/run
$ chmod +x run
$./run Hello
The flag is: picoCTF{REDACTED}
```

Or, we could also just search the strings of the file
```
$ strings run | grep picoCTF
picoCTF{REDACTED}
```