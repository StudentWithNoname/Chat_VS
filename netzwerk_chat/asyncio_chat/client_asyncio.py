import asyncio  # Importiere asyncio für asynchrone Netzwerkkommunikation

# Definiere den Host und den Port für die Verbindung
HOST = '127.0.0.1'  # Lokale IP-Adresse, um sich mit dem Server zu verbinden
PORT = 65434  # Der Port, den der Server überwacht


# Asynchrone Funktion für die Chat-Interaktion
async def chat():
  # Herstellung einer Verbindung zum Server mit einem Reader und Writer
  reader, writer = await asyncio.open_connection(HOST, PORT)
  print(f"[Client] Verbunden mit {HOST}:{PORT}")

  while True:
    # Eingabeaufforderung für die Nachricht des Nutzers
    msg = input("[Client] Nachricht eingeben: ")

    # Bedingung zur Beendigung der Verbindung und Schleife
    if msg.lower() == "exit":
      break

    # Sende die Nachricht an den Server
    writer.write(msg.encode())  # Kodiert die Nachricht als Bytes
    await writer.drain()  # Stellt sicher, dass alle Daten im Puffer gesendet werden

    # Warte auf die Antwort des Servers
    response = await reader.read(100)  # Lese bis zu 100 Bytes
    print(f"[Client] Antwort: {response.decode()}")  # Dekodiere die Antwort und zeige sie an

  # Schließe den Writer sauber, um die Verbindung zu beenden
  writer.close()
  await writer.wait_closed()  # Warte, bis das Schließen der Verbindung abgeschlossen ist


# Starte die asynchrone Chat-Funktion
asyncio.run(chat())
