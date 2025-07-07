import socket  # Importiere das Modul 'socket', um Netzwerkkommunikation zu ermöglichen

# Server-Adresse und Port festlegen
HOST = '127.0.0.1'  # Der lokale Host (localhost) für den Server
PORT = 65432        # Ein frei wählbarer Port für die Verbindung

# Ein TCP/IP-Socket erstellen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Binde das Socket an die Adresse (HOST, PORT)
    s.bind((HOST, PORT))
    # Versetze das Socket in den 'listen'-Modus, um Verbindungsversuche zu akzeptieren
    s.listen()
    print(f"[Server] Lausche auf {HOST}:{PORT} ...")

    # Warten und akzeptieren einer eingehenden Verbindung; blocking call
    conn, addr = s.accept()
    # Verwende das Verbindungs-Socket im Kontextmanager
    with conn:
        print(f"[Server] Verbunden mit {addr}")  # Gib die Adresse des verbundenen Clients aus
        # Endlosschleife zum Empfangen und Versenden von Nachrichten
        while True:
            # Empfange Daten vom Client; bis zu 1024 Bytes
            data = conn.recv(1024)
            # Beende die Schleife, wenn keine Daten empfangen werden
            if not data:
                break
            # Dekodiere die empfangenen Daten in einen String und gib die Nachricht aus
            print(f"[Server] Nachricht empfangen: {data.decode()}")
            # Fordere Eingabe für die Antwort vom Benutzer in der Konsole an
            antwort = input("[Server] Antwort eingeben: ")
            # Senden die Antwort zurück an den Client; die Antwort wird kodiert
            conn.sendall(antwort.encode())
