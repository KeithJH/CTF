MAKEFLAGS += --no-builtin-rules

flag.txt: gdbme_patched.elf
	./gdbme_patched.elf > flag.txt

gdbme_patched.elf: gdbme
	cp gdbme gdbme_patched.elf
	dd of=gdbme_patched.elf bs=1 seek=4902 count=4 conv=notrunc < /dev/zero

gdbme:
	wget https://artifacts.picoctf.net/c/116/gdbme
	chmod +x gdbme

clean:
	rm -f flag.txt gdbme gdbme_patched.elf
