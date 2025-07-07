import asyncio  # Importiert asyncio für asynchrone Netzwerkkommunikation

# Festlegung der Adresse und des Ports des Servers
HOST = '127.0.0.1'  # Der Server soll auf der lokalen IP-Adresse laufen (localhost)
PORT = 65434  # Portnummer, auf der der Server Verbindungen akzeptiert


# Asynchrone Funktion, um mit einem verbundenen Client zu interagieren
async def handle_client(reader, writer):
  addr = writer.get_extra_info('peername')  # Ermittelt die Adresse des verbundenen Clients
  print(f"[Server] Neue Verbindung von {addr}")

  while True:
    # Wartet auf die Nachricht vom Client
    data = await reader.read(100)  # Liest bis zu 100 Bytes von der Client-Nachricht

    if not data:
      # Bedingung zum Beenden der Schleife, wenn keine Daten mehr gesendet werden
      print(f"[Server] Verbindung von {addr} beendet.")
      break

    print(f"[Server] Nachricht: {data.decode()}")  # Dekodiert und zeigt die empfangene Nachricht an

    antwort = input("[Server] Antwort eingeben: ")  # Fordert die Antwort vom Benutzer an der Konsole an
    writer.write(antwort.encode())  # Kodiert die Antwort und sendet sie an den Client
    await writer.drain()  # Stellt sicher, dass der Puffer geleert wird und die Daten gesendet werden

  writer.close()  # Initiieren eines ordnungsgemäßen Schließvorgangs für den Writer
  await writer.wait_closed()  # Warten auf den Abschluss des Schießvorgangs


# Hauptfunktion zur Servereinrichtung
async def main():
  # Initialisiert den Server, um Verbindungen zu akzeptieren und mit Clients zu kommunizieren
  server = await asyncio.start_server(handle_client, HOST, PORT)
  print(f"[Server] Lauscht auf {HOST}:{PORT}")
  async with server:  # Kontextmanager zum ordentlichen Starten und Beenden des Servers
    await server.serve_forever()  # Hält den Server in einem permanenten Zustand, in dem er Anfragen bedient


# Startet den asynchronen Ereignisloop für die Main-Funktion
asyncio.run(main())
