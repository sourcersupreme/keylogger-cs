"""
keylogger — Educational keystroke-capture package.
"""

from .core   import Keylogger
from .config import LOG_FILE, FLUSH_EVERY, ROTATE_KB, TIMESTAMP

__all__ = ["Keylogger", "LOG_FILE", "FLUSH_EVERY", "ROTATE_KB", "TIMESTAMP"]
__version__ = "1.0.0"
