all: server

server:
	gcc -g -o vuln-server vuln-server.c

run-server:
	./vuln-server

run-fuzz:
	python3 fuzz-boofuzz.py