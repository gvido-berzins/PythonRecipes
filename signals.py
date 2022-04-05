"""
Summary:
    Handling process interrupt/termination signals
Description:
    Testing how to handle evens when the system or process is suddenly
    asked to shut down, useful for data processing when the task is half
    finished and state needs to be stored/restored.
References:
    - [signal module docs](https://docs.python.org/3/library/signal.html)
    - [Example code of handler and exceptions](https://docs.python.org/3/library/signal.html)
    - [UNIX signals](https://www.tutorialspoint.com/unix/unix-signals-traps.htm)
Signals:
    SIGTERM (15) - send on system shutdown
    SIGKILL (9) - if the process does not respond to SIGTERM, SIGKILL is sent (only sent, not handled)
    SIGINT (2) - keyboard interrupt (ctrl+c)
Guide:
    $ python signals.py               # Run the server
    $ kill -15 `pgrep -f signals.py`  # Send TERM signal
    $ kill -2 `pgrep -f signals.py`   # INT signal or do CTRL+C
    $ kill -9 `pgrep -f signals.py`   # KILL signal
"""
import sys
import time
from signal import SIGINT, SIGTERM, signal


def print_l(list_: list):
    print("\n-- LIST --\n")
    for el in list_:
        print(el)

    print(f"\nTOTAL LINES: {len(list_)}")
    print("\n-- LIST --\n")


def server_loop():
    errors = []

    def sigterm_handler(signum, frame):
        err = f"TERM received ({signum}, {frame})"
        errors.append(err)
        print_l(errors)

    def sigint_handler(signum, frame):
        err = f"INT received ({signum}, {frame})"
        errors.append(err)
        print_l(errors)
        sys.exit(0)

    signal(SIGTERM, sigterm_handler)
    signal(SIGINT, sigint_handler)
    while True:
        time.sleep(1)


if __name__ == "__main__":
    server_loop()
