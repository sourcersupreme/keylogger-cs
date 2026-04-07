"""
utils.py — Utility helpers: special-key mapping, log rotation, session header.
"""

import os
from datetime import datetime
from pynput import keyboard


# ── Special-key label map ──────────────────────────────────────────────────────

SPECIAL_KEYS: dict = {
    keyboard.Key.space:     " ",
    keyboard.Key.enter:     "\n[ENTER]\n",
    keyboard.Key.backspace: "[BKSP]",
    keyboard.Key.tab:       "[TAB]",
    keyboard.Key.shift:     "[SHIFT]",
    keyboard.Key.shift_r:   "[SHIFT]",
    keyboard.Key.ctrl_l:    "[CTRL]",
    keyboard.Key.ctrl_r:    "[CTRL]",
    keyboard.Key.alt_l:     "[ALT]",
    keyboard.Key.alt_r:     "[ALT]",
    keyboard.Key.caps_lock: "[CAPS]",
    keyboard.Key.delete:    "[DEL]",
    keyboard.Key.esc:       "[ESC]",
    keyboard.Key.up:        "[UP]",
    keyboard.Key.down:      "[DOWN]",
    keyboard.Key.left:      "[LEFT]",
    keyboard.Key.right:     "[RIGHT]",
    keyboard.Key.home:      "[HOME]",
    keyboard.Key.end:       "[END]",
    keyboard.Key.page_up:   "[PGUP]",
    keyboard.Key.page_down: "[PGDN]",
    keyboard.Key.f1:        "[F1]",
    keyboard.Key.f2:        "[F2]",
    keyboard.Key.f3:        "[F3]",
    keyboard.Key.f4:        "[F4]",
    keyboard.Key.f5:        "[F5]",
    keyboard.Key.f6:        "[F6]",
    keyboard.Key.f7:        "[F7]",
    keyboard.Key.f8:        "[F8]",
    keyboard.Key.f9:        "[F9]",
    keyboard.Key.f10:       "[F10]",
    keyboard.Key.f11:       "[F11]",
    keyboard.Key.f12:       "[F12]",
}


def key_label(key) -> str:
    """Return a human-readable string for any key."""
    try:
        return key.char  # printable character
    except AttributeError:
        return SPECIAL_KEYS.get(key, f"[{key.name.upper()}]")


# ── Log helpers ────────────────────────────────────────────────────────────────

def ensure_logs_dir(log_file: str) -> None:
    """Create the logs directory if it doesn't exist."""
    os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)


def session_header() -> str:
    """Return a timestamped session banner."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"\n\n{'='*60}\nSession started : {now}\n{'='*60}\n"


def rotate_if_needed(log_file: str, rotate_kb: int) -> None:
    """
    If *log_file* exceeds *rotate_kb* KB, rename it with a timestamp suffix
    so the next write starts a fresh file.
    """
    if os.path.exists(log_file) and os.path.getsize(log_file) > rotate_kb * 1024:
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        base, ext = os.path.splitext(log_file)
        os.rename(log_file, f"{base}_{ts}{ext}")"""
utils.py — Utility helpers: special-key mapping, log rotation, session header.
"""

import os
from datetime import datetime
from pynput import keyboard


# ── Special-key label map ──────────────────────────────────────────────────────

SPECIAL_KEYS: dict = {
    keyboard.Key.space:     " ",
    keyboard.Key.enter:     "\n[ENTER]\n",
    keyboard.Key.backspace: "[BKSP]",
    keyboard.Key.tab:       "[TAB]",
    keyboard.Key.shift:     "[SHIFT]",
    keyboard.Key.shift_r:   "[SHIFT]",
    keyboard.Key.ctrl_l:    "[CTRL]",
    keyboard.Key.ctrl_r:    "[CTRL]",
    keyboard.Key.alt_l:     "[ALT]",
    keyboard.Key.alt_r:     "[ALT]",
    keyboard.Key.caps_lock: "[CAPS]",
    keyboard.Key.delete:    "[DEL]",
    keyboard.Key.esc:       "[ESC]",
    keyboard.Key.up:        "[UP]",
    keyboard.Key.down:      "[DOWN]",
    keyboard.Key.left:      "[LEFT]",
    keyboard.Key.right:     "[RIGHT]",
    keyboard.Key.home:      "[HOME]",
    keyboard.Key.end:       "[END]",
    keyboard.Key.page_up:   "[PGUP]",
    keyboard.Key.page_down: "[PGDN]",
    keyboard.Key.f1:        "[F1]",
    keyboard.Key.f2:        "[F2]",
    keyboard.Key.f3:        "[F3]",
    keyboard.Key.f4:        "[F4]",
    keyboard.Key.f5:        "[F5]",
    keyboard.Key.f6:        "[F6]",
    keyboard.Key.f7:        "[F7]",
    keyboard.Key.f8:        "[F8]",
    keyboard.Key.f9:        "[F9]",
    keyboard.Key.f10:       "[F10]",
    keyboard.Key.f11:       "[F11]",
    keyboard.Key.f12:       "[F12]",
}


def key_label(key) -> str:
    """Return a human-readable string for any key."""
    try:
        return key.char  # printable character
    except AttributeError:
        return SPECIAL_KEYS.get(key, f"[{key.name.upper()}]")


# ── Log helpers ────────────────────────────────────────────────────────────────

def ensure_logs_dir(log_file: str) -> None:
    """Create the logs directory if it doesn't exist."""
    os.makedirs(os.path.dirname(os.path.abspath(log_file)), exist_ok=True)


def session_header() -> str:
    """Return a timestamped session banner."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"\n\n{'='*60}\nSession started : {now}\n{'='*60}\n"


def rotate_if_needed(log_file: str, rotate_kb: int) -> None:
    """
    If *log_file* exceeds *rotate_kb* KB, rename it with a timestamp suffix
    so the next write starts a fresh file.
    """
    if os.path.exists(log_file) and os.path.getsize(log_file) > rotate_kb * 1024:
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        base, ext = os.path.splitext(log_file)
        os.rename(log_file, f"{base}_{ts}{ext}")
