import socket
import threading

HOST = '127.0.0.1'
PORT = 65433

def empfang(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[Client] Verbindung beendet.")
                break
            print(f"\n[Client] Nachricht empfangen: {data.decode()}")
        except:
            break

def senden(sock):
    while True:
        try:
            msg = input("[Client] Nachricht eingeben: ")
            sock.sendall(msg.encode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"[Client] Verbunden mit Server auf {HOST}:{PORT}")

    threading.Thread(target=empfang, args=(client_socket,), daemon=True).start()
    senden(client_socket)
