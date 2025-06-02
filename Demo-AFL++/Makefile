CC=afl-clang-fast # Note here is the afl++ compiler
CFLAGS=-g -O0

all: example

example: vuln-app.c
	$(CC) $(CFLAGS) -o example vuln-app.c

clean:
	rm -f example
	rm -rf output/*

fuzz: example
	AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1 afl-fuzz -i input -o output -- ./example 
		

.PHONY: all clean fuzz
