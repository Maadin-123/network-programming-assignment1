# File: helpdesk_python.py
# Run server: python helpdesk_python.py server
# Run client: python helpdesk_python.py client

import socket, sys

HOST = "127.0.0.1"
PORT = 5000

def run_server():
    ticket = 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Helpdesk server running on {HOST}:{PORT}")
        while True:
            conn, addr = server.accept()
            with conn:
                request = conn.recv(1024).decode()
                print("Received from", addr, ":", request)
                response = f"Request received. Ticket number: HD{ticket:03d}"
                conn.sendall(response.encode())
                ticket += 1

def run_client():
    reg = input("Registration number: ").strip()
    issue = input("Issue: ").strip()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            client.sendall(f"{reg}: {issue}".encode())
            print(client.recv(1024).decode())
    except ConnectionRefusedError:
        print("Server is not running or is unreachable.")

if len(sys.argv) > 1 and sys.argv[1] == "server":
    run_server()
else:
    run_client()
