import socket
import traceback

LISTEN_IFACE_IP = "192.168.100.20"
FORWARD_TO_IP = "192.168.100.30"
FORWARD_TO_PORT = 9000

def suppress_icmp_unreachable():
    """
    Bind a dummy UDP socket to prevent the OS from sending ICMP 'Port Unreachable'
    messages if no app is listening on the destination port.
    """
    try:
        dummy_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dummy_sock.bind((LISTEN_IFACE_IP, FORWARD_TO_PORT))
        print(f"[*] Dummy UDP socket bound to {LISTEN_IFACE_IP}:{FORWARD_TO_PORT} to suppress ICMP")
    except Exception as e:
        print(f"[!] Error binding dummy socket: {e}")

def start_proxy():
    """
    Start the proxy: receive raw UDP packets and forward them using a normal UDP socket,
    after modifying the payload.
    """
    suppress_icmp_unreachable()

    # Receive all incoming UDP packets (raw socket)
    recv_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    recv_sock.bind((LISTEN_IFACE_IP, 0))

    # Use a standard UDP socket to send the modified packet
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"[*] Raw UDP proxy listening on {LISTEN_IFACE_IP}")

    while True:
        packet, _ = recv_sock.recvfrom(65535)
        ip_header = packet[:20]
        udp_header = packet[20:28]
        payload = packet[28:]

        # Extract source port (for logging only)
        src_port = int.from_bytes(udp_header[0:2], 'big')

        # Modify payload
        modified_payload = b"PROXY" + payload

        # Send modified payload to real receiver
        send_sock.sendto(modified_payload, (FORWARD_TO_IP, FORWARD_TO_PORT))
        print(f"[>] Forwarded {len(modified_payload)} bytes from src_port {src_port} → {FORWARD_TO_IP}:{FORWARD_TO_PORT}")

if __name__ == "__main__":
    try:
        start_proxy()
    except Exception:
        print("[!] Proxy crashed with exception:")
        traceback.print_exc()
        import time
        time.sleep(60)  # Keep container alive for debugging
