MAKEFLAGS += --no-builtin-rules

clean:
	rm -f flag.txt

flag.txt:
	sed -n '378p' leak/passwords.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' > flag.txt
