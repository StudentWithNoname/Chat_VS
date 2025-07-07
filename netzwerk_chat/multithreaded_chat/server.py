import socket
import threading

HOST = '127.0.0.1'
PORT = 65433

def empfang(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("[Server] Verbindung wurde beendet.")
                break
            print(f"\n[Server] Nachricht empfangen: {data.decode()}")
        except:
            break

def senden(conn):
    while True:
        try:
            msg = input("[Server] Nachricht eingeben: ")
            conn.sendall(msg.encode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[Server] Lauscht auf {HOST}:{PORT} ...")
    conn, addr = server_socket.accept()
    print(f"[Server] Verbunden mit {addr}")

    threading.Thread(target=empfang, args=(conn,), daemon=True).start()
    senden(conn)
