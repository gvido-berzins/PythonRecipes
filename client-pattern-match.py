"""
Summary:
    Getting a client based on a match pattern and protocol
"""
from dataclasses import dataclass


@dataclass
class HTTPClient:
    auth: dict


@dataclass
class SMBClient:
    auth: dict


@dataclass
class SSHClient:
    auth: dict


def client_factory(auth: dict):
    protocol = auth.get("protocol")
    match protocol:
        case "http":
            return HTTPClient(auth)
        case "ssh" | "sftp":
            return SSHClient(auth)
        case "smb":
            return SMBClient(auth)
        case _:
            raise NameError(f"No supported client for protocol: {protocol}")


def main():
    auth = dict(protocol="sftp")
    client = client_factory(auth)
    print(client)


if __name__ == "__main__":
    main()
