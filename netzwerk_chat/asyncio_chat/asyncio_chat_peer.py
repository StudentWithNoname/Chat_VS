import asyncio
import argparse

# Funktion zum Empfang von Nachrichten
async def empfangen(reader):
    while True:
        try:
            daten = await reader.readline()
            if not daten:
                print("Verbindung wurde vom Peer getrennt.")
                break
            print(f"\nEmpfangen: {daten.decode().strip()}")
        except Exception as e:
            print(f"Fehler beim Empfangen: {e}")
            break

# Funktion zum Senden von Nachrichten
async def senden(writer):
    loop = asyncio.get_running_loop()
    while True:
        try:
            nachricht = await loop.run_in_executor(None, input, "Nachricht eingeben: ")
            writer.write((nachricht + '\n').encode())
            await writer.drain()
        except Exception as e:
            print(f"Fehler beim Senden: {e}")
            break

# Handler für eingehende Verbindungen (Server-Teil)
async def verbinde_handler(reader, writer):
    print("Peer hat sich verbunden.")
    await empfangen(reader)

# Hauptfunktion
async def main():
    parser = argparse.ArgumentParser(description="AsyncIO P2P Chat")
    parser.add_argument("--listen-port", type=int, required=True, help="Port zum Lauschen")
    parser.add_argument("--peer-ip", type=str, required=True, help="IP-Adresse des Kommunikationspartners")
    parser.add_argument("--peer-port", type=int, required=True, help="Port des Kommunikationspartners")
    args = parser.parse_args()

    # Starte Server (zum Empfangen)
    server = await asyncio.start_server(verbinde_handler, '0.0.0.0', args.listen_port)
    print(f"Warte auf Verbindungen auf Port {args.listen_port}...")

    # Wiederholtes Verbindungsversuchs-Loop
    while True:
        try:
            reader, writer = await asyncio.open_connection(args.peer_ip, args.peer_port)
            print(f"Verbunden mit Peer unter {args.peer_ip}:{args.peer_port}")
            break  # Verbindung erfolgreich, Loop abbrechen
        except Exception as e:
            print(f"Konnte keine Verbindung zum Peer aufbauen: {e}")
            await asyncio.sleep(5)  # Warte 5 Sekunden, bevor ein neuer Versuch gestartet wird

    # Starte Server und Sender gleichzeitig
    async with server:
        await asyncio.gather(
            server.serve_forever(),
            senden(writer)
        )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nChat beendet.")
