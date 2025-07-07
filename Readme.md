# Synchrone und Asynchrone Kommunikation – Chat Beispiel in Python

Dieses Projekt demonstriert die Unterschiede zwischen synchroner und asynchroner Kommunikation anhand von Chat-Programmen in Python.

## 📁 Projektstruktur

```plaintext
chat-tutorial/
│
├── tcp/
│   ├── server.py          # Synchroner TCP-Server
│   └── client.py          # Synchroner TCP-Client
│
├── multithreaded_chat/
│   ├── server.py          # (Optional) Multithreaded-Chat-Server
│   └── client.py          # (Optional) Client für multithreaded Server
│
├── asyncio_chat/
│   ├── server_asyncio.py  # Asynchroner TCP-Server mit asyncio
│   └── client_asyncio.py  # Asynchroner TCP-Client mit asyncio
## 🚀 Schnellstart

🔹 1. Synchroner TCP-Chat (`tcp/`)

Server starten (in neuem Terminal)

python tcp/server.py

Client starten (in neuem Terminal)

python tcp/client.py

🟡 Nur ein Client möglich. Der Server wartet blockierend auf Nachrichten.

⸻

🔹 2. Asynchroner Chat mit asyncio (asyncio_chat/)

Server starten

python asyncio_chat/server_asyncio.py

Client starten (mehrfach in neuen Terminals möglich)

python asyncio_chat/client_asyncio.py

🟢 Mehrere Clients gleichzeitig möglich. Der Server verarbeitet Nachrichten parallel mit asyncio.

⸻

🎯 Ziele des Tutorials
	•	Verständnis von Synchronizität vs. Asynchronizität
	•	Praktische Umsetzung von Chat-Systemen über Netzwerksockets
	•	Demonstration von Blockierung vs. Nebenläufigkeit
	•	Einbettung in das Modul Verteilte Systeme (HTW, WiSe 24/25)

🛠 Voraussetzungen
	•	Python 3.7 oder neuer
	•	Keine externen Pakete notwendig (nur socket, threading, asyncio)

📚 Weiterführende Quellen
	•	Python-Dokumentation: socket
	•	Python-Dokumentation: asyncio
	•	Real Python: Async IO in Python
	•	Vorlesung Verteilte Systeme – HTW Berlin

💡 Tipps zur Nutzung
	•	Verwende mehrere Terminal-Tabs oder -Fenster für Server & Clients.
	•	Beobachte die Unterschiede: synchrone Blockierung vs. asynchrones Multitasking.
	•	Nutze den asynchronen Chat, um mehrere Clients gleichzeitig zu simulieren.

📽️ Präsentation / Video

Dieses Projekt dient als Codebasis für das Video-Tutorial zur Prüfungsvorbereitung. Im Video werden die Grundlagen erläutert und die Funktionsweise der Chat-Systeme demonstriert.

👨‍🏫 Autor:innen
	•	[Stefan Ernes]
	•	[Christopher Mauritz]
	
HTW Berlin – Modul Verteilte Systeme, SoSe 2025

---


