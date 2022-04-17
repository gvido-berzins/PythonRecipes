from dataclasses import dataclass


@dataclass
class Database:
    name: str = "mysql"
    host: str = "127.0.0.1"
    port: int = 3306
    user: str = ""
    passw: str = ""


@dataclass
class Server:
    database: Database
    name: str = "???"
    host: str = "127.0.0.1"
    port: int = 8999


@dataclass
class Client:
    timeout: int = 30
    secret_key: str = "w"


@dataclass
class DefaultConfig:
    server: Server
    client: Client
