# Peer-to-Peer-Kommunikation in Python

Synchrone und Asynchrone Peer-to-Peer-Kommunikation in Python

# Synchrone und Asynchrone Peer-to-Peer-Kommunikation in Python

Dieses Projekt zeigt die Implementierung von synchronen und asynchronen Peer-to-Peer-Chats in Python.

## 📁 Projektstruktur

```plaintext
chat-tutorial/
│
├── tcp/
│   └── peer.py            # Synchroner TCP-Client für peer-to-peer-Kommunikation
│
├── asyncio_chat/
│   └── asyncio_chat_peer.py # Asynchroner Peer-to-Peer-Chat mit asyncio
Schnellstart

1. Synchrone Peer-to-Peer-Kommunikation (tcp/)

Starten Sie den ersten Peer (z.B. Alice):

bash
python peer.py --listen-port 5002 --peer-ip 127.0.0.1 --peer-port 5003


Starten Sie den zweiten Peer (z.B. Bob):

bash
python peer.py --listen-port 5003 --peer-ip 127.0.0.1 --peer-port 5002


Diese Konfiguration ermöglicht es zwei Peers, synchron miteinander zu kommunizieren.

---

2. Asynchrone Peer-to-Peer-Kommunikation (asyncio_chat/)

Starten Sie den ersten Peer (z.B. Alice):

bash
python asyncio_chat_peer.py --listen-port 5002 --peer-ip 127.0.0.1 --peer-port 5003


Starten Sie den zweiten Peer (z.B. Bob):

bash
python asyncio_chat_peer.py --listen-port 5003 --peer-ip 127.0.0.1 --peer-port 5002


Dank der Umsetzung mit `asyncio` ermöglicht dieses Setup den gleichzeitigen Nachrichtenaustausch zwischen zwei Peers, was zu einer effizienteren und reaktionsfähigeren Kommunikation führt.

---

Ziele des Projekts
- Verständnis der Unterschiede zwischen synchroner und asynchroner Kommunikation.
- Praktische Umsetzung von Peer-to-Peer-Systemen über Netzwerksockets.
- Demonstration der Blockierung in synchronen Systemen vs. der Gleichzeitigkeit in asynchronen Systemen.

Voraussetzungen
- Python 3.7 oder neuer.
- Keine externen Pakete notwendig (nur python-integrierte Module: socket, asyncio).

Weiterführende Quellen
- Python-Dokumentation: socket
- Python-Dokumentation: asyncio

Tipps zur Nutzung
- Öffnen Sie mehrere Terminal-Tabs oder -Fenster, um die Peers zu starten.
- Achten Sie auf den Unterschied in der Antwortzeit und Effizienz zwischen den synchronen und asynchronen Modellen.
- Experimentieren Sie mit verschiedenen Nachrichten, um das Potenzial der asynchronen Kommunikation zu erkunden.

Autor:innen
- [Stefan Ernes]
- [Christopher Mauritz]

HTW Berlin – Modul Verteilte Systeme, SoSe 2025
