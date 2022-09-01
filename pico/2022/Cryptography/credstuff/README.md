# credstuff
## Description
- **Tags**:
    - picoCTF 2022
    - Cryptography
- **Author**:
    - Will Hong
    - LT 'Syreal' Jones


We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?

Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar).

The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

## Exploration
Taking a look at the provied tar file we're presented with two files as described. Let's extract those out so we can work on them.
```
$ tar -tf leak.tar
leak/
leak/passwords.txt
leak/usernames.txt

$ tar -xf leak.tar
```

We can then go ahead and identify the line number of the "cultiris" user in usernames.txt and find the corresponding line number from passwords.txt.
```
$ grep -n cultiris leak/usernames.txt
378:cultiris

$ head -n 378 leak/passwords.txt | tail -n 1
cvpbPGS{P7e1S_54I35_71Z3}

$ sed -n '378p' leak/passwords.txt
cvpbPGS{P7e1S_54I35_71Z3}

$ awk 'NR==378' leak/passwords.txt
cvpbPGS{P7e1S_54I35_71Z3}
```

Since we know the expected format of a flag we can try and compare against expected values. It looks like symbols haven't been changed, but at least the alphabet has. Let's see if we can notice any trends. Conveniently it seems like all the characters are 13 values apart. Seems like a good first guess, as this is now feeling like ROT13.
```python
>>> expected = 'picoCTF'
>>> given = 'cvpbPGS'
>>> for e, g in zip(expected, given):
...     print(ord(e) - ord(g))
...
13
-13
-13
13
-13
13
-13
```

Taking a quick look, we get a sane output.
```
$ sed -n '378p' leak/passwords.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' 
picoCTF{REDACTED}
```