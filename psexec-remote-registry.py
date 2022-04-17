"""
Summary:
    Remotly download registry (or just execute commands) using psexec (SMB)
Description:
    I wanted to script a quick recipe to run commands on windows, so I found this post https://www.bloggingforlogging.com/2018/03/12/introducing-psexec-for-python/
    thanks to Jordan Borean for the resource
"""

import os
from argparse import ArgumentParser
from contextlib import contextmanager

from dotenv import load_dotenv
from pypsexec.client import Client

load_dotenv()


def parse_args():
    parser = ArgumentParser(
        description="Simple Python script to execute windows commands over SMB"
    )
    parser.add_argument("exe", help="Executable")
    parser.add_argument("arguments", default="", nargs="?", help="Arguments")
    return parser.parse_args()


@contextmanager
def psexec_session(c: Client):
    c.connect()
    try:
        c.create_service()
        yield c

    finally:
        c.remove_service()
        c.disconnect()


def main():
    server = os.environ["PSX_HOST"]
    username = os.environ["PSX_USER"]
    password = os.environ["PSX_PASS"]
    exe, arguments = args.exe, args.arguments
    client = Client(server, username=username, password=password)
    with psexec_session(client):
        result = client.run_executable(exe, arguments)
        print("STDOUT:\n%s" % result[0].decode("utf-8") if result[0] else "")
        print("STDERR:\n%s" % result[1].decode("utf-8") if result[1] else "")
        print("RC: %d" % result[2])


if __name__ == "__main__":
    args = parse_args()
    main()
