# Network Fuzzing Proof-of-Concepts

This repository contains a collection of proof-of-concept (PoC) setups for fuzzing network-based applications using different techniques and tools. Each subfolder targets a different protocol or fuzzing engine, providing isolated examples for testing and learning purposes.

---

## 🔧 Repository Structure

### `Demo-AFL++`
A basic example demonstrating how to set up and run fuzzing using AFL++ on a minimal C/C++ application. Useful for understanding instrumentation and fuzzing loop setup.


### `POC-Socket-AFL++`
A more advanced example using AFL++ with a socket-based application. Demonstrates how to fuzz a service that listens on TCP or UDP, with AFL's forkserver integration.

### `POC-Socket-BooFuzz`
A proof-of-concept using [BooFuzz](https://github.com/jtpereyda/boofuzz), a Python-based fuzzing framework. This project shows how to define fuzzing sessions for custom socket protocols.

### `POC-UDP-Raw-Socket-Fuzzing`
A raw socket-based UDP fuzzer. Uses Docker containers to simulate sender, proxy, and receiver. The proxy intercepts UDP packets using raw sockets and modifies fields like TTL, ports, and checksums in real time.

---

## 🚀 Goals

- Explore different approaches to fuzzing (instrumented, generational, network-level)
- Compare tools like AFL++, BooFuzz, and manual raw-socket manipulation
- Provide minimal, reproducible examples that can be reused or extended

---

## 📦 Requirements

- Docker
- Python 3.8+
- AFL++ (if testing AFL folders)
- Linux (raw sockets and iptables setup may require root privileges and NET_ADMIN capability)

---

## 🔍 Usage

Each folder contains its own `README.md` and `start.py` (or equivalent) with setup instructions. You can explore them independently based on your interest:

