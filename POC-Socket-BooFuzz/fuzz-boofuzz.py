# fuzz-boofuzz.py
from boofuzz import *

def main():
    while True:
        try:
            session = Session(
                target=Target(
                    connection=SocketConnection("127.0.0.1", 9002, proto='tcp')
                )
            )
            s_initialize("fuzz_input")
            s_string("HELLO", fuzzable=True)

            session.connect(s_get("fuzz_input"))
            session.fuzz()
        except Exception as e:
            print(f"[!] Fuzzing error or crash detected: {e}")
            continue

if __name__ == "__main__":
    main()
