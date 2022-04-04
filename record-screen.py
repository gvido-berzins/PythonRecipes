#!/usr/bin/env python3
"""
Summary:
    Simple screen recorder script for a Linux based OS
Description:
    The command strings for Popen can be easily adjusted for Mac OS and Windows.
    This script can be used in a CI or anywhere else, I had an edge case where I
    couldn't use library for doing automated UI tests and needed a foolproof way
    to see what's going on.
"""
import sys
from pathlib import Path
from subprocess import Popen
from time import sleep

WATCH_FILE = Path("wa")


def start_recorder():
    display = sys.argv[-1] if len(sys.argv) > 1 else 99
    recorder_process = Popen(
        f"ffmpeg -y -f x11grab -s 1920x1080 -i :{display}.0 video.mkv".split()
    )
    WATCH_FILE.write_text("0")
    return recorder_process


def watch_for_killevent(recorder_process):
    while True:
        should_kill = WATCH_FILE.read_text().strip()
        if should_kill == "1":
            recorder_process.terminate()
        sleep(0.3)


def main():
    recorder_process = start_recorder()
    watch_for_killevent(recorder_process)


if __name__ == "__main__":
    main()
