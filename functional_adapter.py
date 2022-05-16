"""
Summary:
    Adapter pattern using a functional programming approach
Description:
    Learned from watching a [video from ArjanCodes](https://www.youtube.com/watch?v=fsB8_79zI_A)
Requires:
    - `pip install lxml, beautifulsoup4`"""
import functools
import json
from typing import Any, Callable

from bs4 import BeautifulSoup

XML_CONFIG = """<?xml version="1.0" ?><config>
<host>127.0.0.1</host><port>9001</port></config>"""
JSON_CONFIG = '{ "host": "127.0.0.1", "port": "9001" }'

ConfigGetter = Callable[[str], Any | None]


class App:
    def __init__(self, config_getter: ConfigGetter):
        """Receives config getter to access the config keys

        Example:
        - `config_getter("key")`"""
        self.config_getter = config_getter

    def start(self):
        host = self.config_getter("host")
        port = self.config_getter("port")
        print(f"Starting App on: {host}:{port}")


def get_xml_config(path: str, key: str, default: Any = None) -> Any | None:
    print(f"Reading XML from '{path}'")
    config = XML_CONFIG  # Pretending to read config from `path` using `f.read()`
    bs = BeautifulSoup(config, "xml")
    value = bs.find(key)
    if not value:
        return default
    return value.get_text()


def get_json_config(path: str, key: str, default: Any = None) -> Any | None:
    print(f"Reading JSON from '{path}'")
    # Pretending to read config from `path` using `json.loads(file)`
    config = json.loads(JSON_CONFIG)
    return config.get(key, default)


def adapter_factory(path: str) -> ConfigGetter:
    if path.endswith("xml"):
        getter = functools.partial(get_xml_config, path)
    elif path.endswith("json"):
        getter = functools.partial(get_json_config, path)
    else:
        raise ValueError(f"No adapter for config '{path}'")
    return getter


def main() -> int:
    config_getter = adapter_factory("config.xml")
    app = App(config_getter)
    app.start()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
