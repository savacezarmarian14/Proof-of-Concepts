```markdown
# PoC - UDP Raw Socket Fuzzing with iptables Redirection

This proof of concept demonstrates how to intercept and modify UDP packets using raw sockets in a containerized setup. The traffic is redirected to a proxy using `iptables` DNAT rules, and the proxy modifies specific fields of the IP/UDP header before forwarding the packet to the receiver.

---

## Architecture

- **udpsender**: sends UDP packets continuously to a fixed IP and port  
- **proxy**: receives those packets via DNAT, modifies them using raw sockets, and forwards them  
- **udpreceiver**: receives the modified packets and logs them  

```
+-----------+            +--------+            +-------------+
| udpsender | --UDP-->   | proxy  | --UDP-->   | udpreceiver |
|  .100.2   |            | .100.3 |            |   .100.4     |
+-----------+            +--------+            +-------------+
          \__________________________________/
               Redirected by iptables DNAT
```

---

## Setup and Usage

### 1. Clone the repo

```bash
git clone <this_repo>
cd POC-UDP-Raw-Socket-Fuzzing
```

### 2. Build and start everything

```bash
python3 start.py
```

This script will:
- Create a Docker network `udp-net` with static IPs
- Build all three Docker images
- Start each container with the correct IP
- Add the DNAT rule in the proxy to intercept UDP packets on port `9000`

---

## Log Access

To view logs for each component, use:

```bash
docker logs sender
docker logs proxy
docker logs receiver
```

Or for live logs:

```bash
docker logs -f proxy
```

---

## Proxy Behavior

The proxy:
- Listens with a raw socket
- Parses the IP and UDP headers
- Modifies one random field: `ttl`, `id`, `src_port`, `dst_port`, `length`, or `checksum`
- Appends `"proxy-"` to the original payload
- Recomputes the IP checksum
- Sends the modified packet to the real receiver

You will see structured logs showing the original and modified field values, like:

```
[MODIFIER] Randomly modifying field: src_port
  Src Port: 12345 -> 54321
```

---

## Stop and Clean Up

To stop everything and remove the network:

```bash
docker rm -f sender proxy receiver
docker network rm udp-net
```
```
