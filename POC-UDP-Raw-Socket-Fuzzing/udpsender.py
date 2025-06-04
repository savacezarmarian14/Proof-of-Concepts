import socket
import time

DEST_IP = "192.168.100.30"  # Receiver-ul real
DEST_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = b"Hello from sender"
    sock.sendto(msg, (DEST_IP, DEST_PORT))
    print(f"[SENDER] Sent: {msg}")
    time.sleep(1)
