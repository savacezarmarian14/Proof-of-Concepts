# Proof of Concepts

This repository contains a growing collection of **small, self-contained Proof of Concept (PoC) projects** related to systems programming, security, network experimentation, and more.

These PoCs are part of my ongoing personal and academic journey in exploring how things work at a lower level, how they break, and how they can be improved or understood better.

Some of these experiments are connected to my academic work, such as the dissertation project available here: [cezfuzzer](https://github.com/savacezarmarian14/cezfuzzer/)

## 📁 Structure

### [`Demo-AFL++`](./Demo-AFL++)
A simple C binary demonstrating the basics of **AFL++ fuzzing** via standard input. Useful for understanding instrumentation and crash detection.

> 💡 Includes:
> - Source code (`vuln-app.c`)
> - Input corpus
> - Makefile & run instructions
> - Crash logs

### [`POC-Socket-AFL++`](./POC-Socket-AFL++)
A minimal socket-based client-server app fuzzed using AFL++. Highlights difficulties when applying traditional fuzzers to socket communication.

> 💡 Includes:
> - Vulnerable TCP server
> - AFL-instrumented TCP client
> - Wrapper + fuzzing strategy
> - Errors, limitations, and key findings

## 📌 Purpose
The goal of this repository is to:
- Provide hands-on, minimal PoCs that explore deep technical concepts
- Build a portfolio of technical experiments across areas like fuzzing, networking, protocol testing, binary analysis, etc.
- Document and share lessons learned along the way

## 🛠️ Requirements (for current PoCs)
- Linux-based environment (tested on WSL2 Ubuntu 22.04)
- Developer tools: `make`, `gcc`, `clang`, etc.
- Some PoCs may use tools like AFL++, gdb, Wireshark, etc.

## 🧭 Roadmap
Planned and upcoming PoCs:
- UDP socket fuzzing
- MITM socket-based fuzzing
- Custom logging infrastructure
- Reverse engineering mini-tests
- Protocol crafting experiments
- CTF-style vulnerability simulations

---

Feel free to explore, learn, or adapt these PoCs for your own research or projects.
