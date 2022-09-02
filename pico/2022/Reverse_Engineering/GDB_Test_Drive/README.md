# GDB Test Drive
## Description
- **Tags**:
    - picoCTF 2022
    - Reverse Engineering
    - binary
    - gdb
- **Author**: LT 'Syreal' Jones

Can you get the flag?

Download this [binary](https://artifacts.picoctf.net/c/116/gdbme).

Here's the test drive instructions:
```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

## Exploration

```
$ wget https://artifacts.picoctf.net/c/116/gdbme

$ file ./gdbme
./gdbme: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4a97837ebdcca2413f854f9274b4dc31f16f2aee, for GNU/Linux 3.2.0, not stripped

$ checksec ./gdbme
[*] '/home/keithjh/src/CTF/pico/2022/Reverse_Engineering/GDB_Test_Drive/gdbme'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

From here we can just follow the instructions layed out to skip the sleep statement in the program and output the flag.

### Bonus Points
If we want to be a bit fancier we can also patch the binary so that either the sleep call does not exist or we reduce the length of the sleep. To get a value to search for we can disassemble the code to identify the parameter used (0x186a0).

```
$ gdb ./gdbme
gef➤  disassemble main
...
0x0000000000001325 <+94>:    mov    edi,0x186a0
0x000000000000132a <+99>:    call   0x1110 <sleep@plt>
```

We then need to identify where that is in the binary. Thankfully there's only one sequence of these bits present.

```
$ LC_ALL=c grep -oaPb '\xa0\x86\x01\x00' ./gdbme
4902:��
```

We can then write some zeroes and attempt to run the program
```
$ dd of=gdbme bs=1 seek=4902 count=4 conv=notrunc < /dev/zero
$ ./gdbme
picoCTF{REDACTED}
```