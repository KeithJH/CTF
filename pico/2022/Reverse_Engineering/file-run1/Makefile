MAKEFLAGS += --no-builtin-rules

flag.txt: run
	strings run | grep picoCTF > flag.txt

run:
	wget https://artifacts.picoctf.net/c/309/run

clean:
	rm -f flag.txt
