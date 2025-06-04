# receiver.py
import socket

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

print(f"[RECEIVER] Listening on {LISTEN_IP}:{LISTEN_PORT}")

while True:
    data, addr = sock.recvfrom(2048)
    print(f"[RECEIVER] Received from {addr}: {data}")
