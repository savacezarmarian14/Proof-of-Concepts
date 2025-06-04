import subprocess
import time
import os

def run(cmd):
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, shell=True, check=True)

import json
import subprocess

def get_docker_bridge_for_network(network_name: str) -> str:
    out = subprocess.check_output(f"docker network inspect {network_name}", shell=True)
    info = json.loads(out)
    bridge = info[0]["Options"].get("com.docker.network.bridge.name")
    return bridge if bridge else "br-" + info[0]["Id"][:12]

def add_dnat_rule():
    bridge = get_docker_bridge_for_network("udp-net")
    cmd = (
        f"iptables -t nat -A PREROUTING -i {bridge} -p udp "
        f"-d 192.168.100.30 --dport 9000 "
        f"-j DNAT --to-destination 192.168.100.20:9000"
    )
    print(f"[RUN] {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# după pornirea containerelor

def write_dockerfile(filename: str, script: str):
    with open(filename, "w") as f:
        f.write(f"""\
FROM python:3.9-slim

RUN apt-get update && apt-get install -y iptables tcpdump && apt-get clean

COPY {script} /app.py
CMD ["python", "/app.py"]
""")

def wait_for_container(name):
    for _ in range(10):
        try:
            out = subprocess.check_output(f"docker exec {name} echo ok", shell=True)
            if b"ok" in out:
                return
        except subprocess.CalledProcessError:
            time.sleep(1)
    raise RuntimeError(f"Container {name} not responding")

def main():
    print("[*] Creating Docker network...")
    run("docker network create --subnet=192.168.100.0/24 udp-net || true")

    print("[*] Writing Dockerfiles...")
    write_dockerfile("Dockerfile.sender", "udpsender.py")
    write_dockerfile("Dockerfile.proxy", "proxy.py")
    write_dockerfile("Dockerfile.receiver", "udpreceiver.py")

    print("[*] Building Docker images...")
    run("docker build -f Dockerfile.sender -t udpsender .")
    run("docker build -f Dockerfile.proxy -t udpproxy .")
    run("docker build -f Dockerfile.receiver -t udpreceiver .")

    print("[*] Running containers...")
    run("docker run -dit --rm --name receiver --net udp-net --ip 192.168.100.30 udpreceiver")
    run("docker run -dit --rm --name proxy --net udp-net --ip 192.168.100.20 --cap-add=NET_ADMIN --cap-add=NET_RAW udpproxy")
    run("docker run -dit --rm --name sender --net udp-net --ip 192.168.100.10 --cap-add=NET_ADMIN --cap-add=NET_RAW --user root udpsender")

    add_dnat_rule()


    wait_for_container("proxy")
    print("[✅ DONE] All containers started. Proxy will auto-configure iptables from within.")

if __name__ == "__main__":
    main()
