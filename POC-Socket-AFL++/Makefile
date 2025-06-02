# Compilatori
CC=afl-clang-fast
SERVER_CC=gcc

# Flaguri
CFLAGS=-O0 -g

# Binare
CLIENT=afl-client
SERVER=vuln-server

# Surse
CLIENT_SRC=afl-client.c
SERVER_SRC=vuln-server.c

# Directoare fuzz
INPUT=input
OUTPUT=output

.PHONY: all clean run-server run-client fuzz

all: $(CLIENT) $(SERVER)

$(CLIENT): $(CLIENT_SRC)
	$(CC) $(CFLAGS) -o $(CLIENT) $(CLIENT_SRC)

$(SERVER): $(SERVER_SRC)
	$(SERVER_CC) $(CFLAGS) -o $(SERVER) $(SERVER_SRC)

run-server: $(SERVER)
	@echo "Starting vuln-server on port 9001..."
	@./$(SERVER)

run-client: $(CLIENT)
	@echo "Running afl-client with example input..."
	@echo "ABC" | ./$(CLIENT)

fuzz: $(CLIENT)
	@mkdir -p $(INPUT) $(OUTPUT)
	@echo "XYZ" > $(INPUT)/testcase
	AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1 \
	afl-fuzz -t 3000 -i input -o output -- ./afl-client

clean:
	rm -f $(CLIENT) $(SERVER)
	rm -rf $(INPUT) $(OUTPUT)
