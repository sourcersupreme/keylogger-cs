# 🔐 Keylogger — Cybersecurity Educational Project

A clean, well-structured Python keylogger built for **security research and learning**.  
Understand how keystroke capture works at the OS level — and how defenders detect it.

> ⚠️ **Legal notice:** Only run this on systems you own or have **explicit written permission** to test. Unauthorized keylogging is illegal in most jurisdictions.

---

## 📁 Project Structure

```
keylogger-cs/
├── keylogger/
│   ├── __init__.py      # Package exports
│   ├── config.py        # All tuneable settings
│   ├── core.py          # Keylogger class (capture + buffering)
│   └── utils.py         # Key-label map, log rotation, helpers
├── logs/
│   └── .gitkeep         # Folder tracked; log files are gitignored
├── main.py              # CLI entry point (argparse)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

```bash
# 1. Clone
git clone https://github.com/<you>/keylogger-cs.git
cd keylogger-cs

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
# Run with defaults (logs to logs/keylog.txt, press ESC to stop)
python main.py

# Custom log path
python main.py --log logs/session1.txt

# Flush buffer every 5 keystrokes, rotate at 200 KB
python main.py --flush 5 --rotate 200

# Omit session timestamp header
python main.py --no-timestamp
```

### CLI flags

| Flag | Default | Description |
|---|---|---|
| `--log PATH` | `logs/keylog.txt` | Output log file path |
| `--flush N` | `10` | Flush to disk every N keystrokes |
| `--rotate KB` | `500` | Rotate log when it exceeds this KB size |
| `--no-timestamp` | off | Omit session header |

---

## 📖 How It Works

| Component | Role |
|---|---|
| `pynput.keyboard.Listener` | Registers an OS-level hook for key-down/key-up events |
| `on_press` callback | Converts each raw key event to a human-readable label |
| In-memory buffer | Collects labels; flushes to disk every N keys (reduces I/O) |
| Log rotation | Renames the log file with a timestamp when it exceeds the size limit |
| `threading.Lock` | Guards the shared buffer against race conditions |

### Sample log output

```
============================================================
Session started : 2025-08-10 14:32:01
============================================================
hello [SPACE] world[ENTER]
this [SPACE] is [SPACE] a [SPACE] test[BKSP][BKSP][BKSP][BKSP]
```

---

## 🧩 Extend It (Learning Ideas)

- **Email exfiltration simulation** — send the log via `smtplib` on a local test server (e.g., MailHog)
- **Clipboard monitoring** — add `pyperclip` to capture copy/paste events
- **Screenshot on trigger** — use `Pillow` to capture the screen when a hotkey is pressed
- **Write the detector** — build a companion script that scans running processes for active keyboard hooks
- **AV/EDR evasion study** — run inside a VM and observe how security tools flag the process

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [`pynput`](https://pynput.readthedocs.io/) — cross-platform keyboard listener

---

## 📜 License

MIT — free to use for educational and authorized security research purposes.
