"""
config.py — Central configuration for the keylogger project.
Edit these values before running; no other file needs to change.
"""

import os

# ── Logging ────────────────────────────────────────────────────────────────────
LOGS_DIR    = os.path.join(os.path.dirname(__file__), "..", "logs")
LOG_FILE    = os.path.join(LOGS_DIR, "keylog.txt")

FLUSH_EVERY = 10      # Flush buffer to disk every N keystrokes
ROTATE_KB   = 500     # Rotate log file when it exceeds this size (KB)
TIMESTAMP   = True    # Write a session header with date/time on start
