import socket  # Importiere das socket-Modul, um eine Netzwerkschnittstelle zu verwenden

# Definiere den Host und den Port
ZielIp = '127.0.0.1'  # Zielhost, auf den sich der Client verbindet (localhost für lokale Verbindungen)
ZielPort = 65432  # Port, der für die Kommunikation mit dem Server verwendet wird; muss mit dem Server übereinstimmen

# Erstelle ein TCP/IP-Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Verbinde das Socket mit dem Host und dem Port des Servers
    s.connect((ZielIp, ZielPort))
    print(f"[Client] Verbunden mit Server auf {ZielIp}:{ZielPort}")

    # Endlosschleife für den Nachrichtenversand und Empfang
    while True:
        # Benutzeraufforderung zur Eingabe einer Nachricht
        nachricht = input("[Client] Nachricht eingeben: ")

        # Bedingung für das Beenden der Kommunikation
        if nachricht.lower() == "exit":
            break  # Aus der Schleife ausbrechen und die Verbindung beenden

        # Senden der eingegebenen Nachricht an den Server
        s.sendall(nachricht.encode())  # Konvertiere die Nachricht in Bytes und sende sie durch das Socket

        # Empfang der Antwort vom Server
        daten = s.recv(1024).decode()  # Empfange bis zu 1024 Bytes, dekodiere die empfangenen Bytes wieder in einen String

        # Ausgabe der empfangenen Antwort an den Benutzer
        print(f"[Client] Antwort vom Server: {daten}")
