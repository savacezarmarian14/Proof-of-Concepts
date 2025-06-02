# AFL++ Proof-of-Concept: Socket-based Fuzzing !!! [CONCEPT IS NOT PROVED] !!!

This repository demonstrates how to use **AFL++** to fuzz a vulnerable C server application that receives data via **TCP sockets**. Since AFL++ expects to work with `stdin`, we use a Python wrapper to send AFL-generated input over the network.

## Structure

- `server.c` – A vulnerable TCP server that crashes when it receives input starting with "FUZ"
- `afl-client.py` – Python wrapper that reads stdin and sends it over TCP
- `input/testcase` – Initial seed file for fuzzing

## Setup & Usage

### 1. Build the vulnerable server

```bash
make server
make fuzz
```

