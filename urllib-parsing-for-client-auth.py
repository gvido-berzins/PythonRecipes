"""
Summary:
    Parsing given paths into pieces and choosing the correct client
"""
import socket
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import ParseResultBytes, urlparse

import paramiko
import smb
from smb.SMBConnection import SMBConnection

URL = "127.0.0.1"


requests = [
    {"path": f"{URL}/y/screen.mov", "protocol": "http"},
    {"path": f"{URL}/y/screen.mov", "protocol": "ftp"},
    {"path": f"{URL}/y/screen.mov", "protocol": "smb"},
    {"path": f"anon@{URL}/y/screen.mov", "protocol": "smb"},
    {"path": f"anon:Passw123@{URL}:9001/y/screen.mov", "protocol": "smb"},
    {"path": f"http://{URL}/y/screen.mov"},
    {"path": f"http://{URL}:9001/y/screen.mov"},
    {"path": f"ftp://{URL}/y/screen.mov"},
    {"path": f"smb://{URL}/y/screen.mov"},
    {"path": f"ftp://username:password@{URL}/y/screen.mov"},
    {"path": f"ftp://username@{URL}/y/screen.mov"},
    {"path": f"smb://super.server.at.enterprise.tk/y/screen.mov"},
    {"path": f"smb://super.server.at.enterprise.tk:9001/y/screen.mov"},
    {"path": f"smb://User123:p123@super.server.acme.tk:9001/y/screen.mov"},
    {"path": f"ssh://{URL}/api?file=m.mov"},
    {"path": f"ssh://{URL}/api?file=m.mov&auth=pass"},
    {
        "path": f"ssh://{URL}/home/temp/m.mov",
        "auth": {"username": "temp", "password": "pass"},
    },
    {"path": f"smb://{URL}/myshare/screen.mov"},
]


@dataclass
class BasicAuth:
    credential: str


@dataclass
class PasswordAuth:
    username: str
    password: str

    @property
    def empty(self):
        return not self.username and not self.password

    @property
    def unpacked(self):
        return dict(username=self.username, password=self.password)


@dataclass
class Client(ABC):
    @abstractmethod
    def download(self, parsed_url: ParseResultBytes, auth: dict = {}):
        ...


@dataclass
class HTTPClient(Client):
    def download(self, parsed_url: ParseResultBytes, auth: dict = {}):
        ...


@dataclass
class FTPClient(Client):
    def download(self, parsed_url: ParseResultBytes, auth: dict = {}):
        ...


@dataclass
class SMBClient(Client):
    def download(self, parsed_url: ParseResultBytes, auth: PasswordAuth = None):
        try:
            conn = SMBConnection("", "", "localn", "servern")
            conn.connect(parsed_url.netloc, 445)
            path = Path(parsed_url.path)
            share = path.parts[1]
            file_path = "/".join(path.parts[2:])
            res = conn.getAttributes(share, file_path)
            print("Downloaded:", res)
        except smb.smb_structs.OperationFailure:
            print("Couldn't download, {parsed_url.path}")
        except socket.gaierror:
            print("Name or service not known")
        finally:
            conn.close()


@dataclass
class SSHClient(Client):
    def download(self, parsed_url: ParseResultBytes, auth: PasswordAuth = None):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        try:
            auth_dict = auth if isinstance(auth, dict) else auth.unpacked
            print(auth_dict)
            client.connect(parsed_url.netloc, **auth_dict)
            stdin, stdout, stderr = client.exec_command("whoami")
            print(stdout.read())
        except socket.gaierror:
            print("Could not connect to SSH")
        except paramiko.ssh_exception.AuthenticationException:
            print("Could not authenticate")
        finally:
            client.close()


def auth_factory(auth_options: dict):
    option_keys = sorted(list(auth_options.keys()))
    match option_keys:
        case ["credentials", *_]:
            credentials = auth_options.get("credentials", "")
            return BasicAuth(credentials)
        case ["password", "username", *_]:
            username = auth_options.get("username", "")
            password = auth_options.get("password", "")
            return PasswordAuth(username, password)
        case _:
            return {}
            # raise ValueError("Authentication not supported")


def client_factory(scheme: str) -> Client:
    match scheme:
        case "http":
            return HTTPClient()
        case "ftp" | "sftp":
            return FTPClient()
        case "smb":
            return SMBClient()
        case "ssh":
            return SSHClient()
        case _:
            raise NameError(f"No supported client for protocol: {scheme}")


def parse_url(url: str, scheme: str = "") -> ParseResultBytes:
    """Parse a given url and protocol into a ParseResultBytest object"""
    parse_result = urlparse(url)
    if parse_result.scheme == "" and scheme != "":
        parse_result = urlparse(f"{scheme}://{url}")
    if parse_result.netloc == "" and scheme != "":
        parse_result = urlparse(f"{scheme}://{parse_result.path}")
    return parse_result


def print_parsed_result(res: ParseResultBytes, *args, ljust=10, center=50):
    print("PARSED".center(center, "-"))
    print("PROTOCOL".ljust(ljust), ":", res.scheme)
    print("URL".ljust(ljust), ":", res.netloc)
    print("PATH".ljust(ljust), ":", res.path)
    for i, arg in enumerate(args, start=1):
        print(f"ARG {i}".ljust(ljust), ":", arg)

    print()


def main():
    for request in requests:
        path = request.get("path")
        protocol = request.get("protocol", "")
        res = parse_url(path, protocol)
        client = client_factory(res.scheme)
        auth = auth_factory(request.get("auth", {}))
        print_parsed_result(res, client)
        client.download(parsed_url=res, auth=auth)


if __name__ == "__main__":
    main()
