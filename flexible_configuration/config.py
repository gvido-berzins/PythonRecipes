import functools
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, List, Tuple, Type, TypeVar, Union, cast

import yaml

try:
    from . import global_settings as DEFAULTS
except ImportError:
    import global_settings as DEFAULTS

T = TypeVar("T")
StrPath = Union[str, Path]
OptStrPath = Union[None, StrPath]
GenericCallable = Callable[[Any], Any]


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    if not isinstance(x, int) and not isinstance(x, bool):
        if x:
            try:
                x = int(x)
            except ValueError:
                raise Exception("Integer not convertable to string")
        else:
            raise Exception(f"Empty integer given: '{x}'")
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Endpoints:
    get: List[str] = field(default_factory=list)
    post: List[str] = field(default_factory=list)
    delete: List[str] = field(default_factory=list)
    put: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, obj: Any) -> "Endpoints":
        assert isinstance(obj, dict)
        get = from_list(from_str, obj.get("get", DEFAULTS.GET_ENDPOINTS))
        post = from_list(from_str, obj.get("post", DEFAULTS.POST_ENDPOINTS))
        delete = from_list(from_str, obj.get("delete", DEFAULTS.DELETE_ENDPOINTS))
        put = from_list(from_str, obj.get("put", DEFAULTS.PUT_ENDPOINTS))
        return Endpoints(get, post, delete, put)

    def to_dict(self) -> dict:
        result: dict = {}
        result["get"] = from_list(from_str, self.get)
        result["post"] = from_list(from_str, self.post)
        result["delete"] = from_list(from_str, self.delete)
        result["put"] = from_list(from_str, self.put)
        return result


@dataclass
class Server:
    host: str = "127.0.0.1"
    port: int = 9001

    @classmethod
    def from_dict(cls, obj: Any) -> "Server":
        assert isinstance(obj, dict)
        host = from_str(obj.get("host", cls.host))
        port = from_int(obj.get("port", cls.port))
        return Server(host, port)

    def to_dict(self) -> dict:
        result: dict = {}
        result["host"] = from_str(self.host)
        result["port"] = from_int(self.port)
        return result


@dataclass
class Config:
    server: Server
    endpoints: Endpoints
    env: str = "test"

    @classmethod
    def from_dict(cls, obj: Any) -> "Config":
        assert isinstance(obj, dict)
        env = from_str(obj.get("env", cls.env))
        server = Server.from_dict(obj.get("server"))
        endpoints = Endpoints.from_dict(obj.get("endpoints"))
        return Config(server, endpoints, env)

    def to_dict(self) -> dict:
        result: dict = {}
        result["env"] = from_str(self.env)
        result["server"] = to_class(Server, self.server)
        result["endpoints"] = to_class(Endpoints, self.endpoints)
        return result


def config_from_dict(s: Any) -> Config:
    return Config.from_dict(s)


def config_to_dict(x: Config) -> dict:
    return to_class(Config, x)


def str_to_path(path: StrPath) -> Path:
    if isinstance(path, str):
        path = Path(path)
    return path


def load_yaml(path: StrPath):
    path = str_to_path(path)
    return yaml.safe_load(path.read_text())


def get_work_config():
    config_path = DEFAULTS.WORK_CONFIG_PATH
    if not config_path.exists():
        print("Work config doesn't exist configuring the default")
        configure()

    return load_yaml(config_path)


def create_work_config(config_obj: Config):
    config_path = DEFAULTS.WORK_CONFIG_PATH
    dict_ = config_to_dict(config_obj)
    yaml_str = yaml.safe_dump(dict_)
    config_path.write_text(yaml_str)


def get_config(path: OptStrPath = None) -> Config:
    if path:
        yaml_data = load_yaml(path)
    else:
        yaml_data = get_work_config()
    return config_from_dict(yaml_data)


def _set_if_value(setter: GenericCallable, value: Any, as_type: GenericCallable = str):
    if value:
        setter(as_type(value))


def _find_config_path(path: OptStrPath) -> Path:
    if path:
        # Using custom config
        path = str_to_path(path)
        if not path.exists():
            print("Given configuration does not exist using default")
            from_path = DEFAULTS.DEFAULT_CONFIG_PATH
        else:
            from_path = path
    else:
        # Using default config
        from_path = DEFAULTS.DEFAULT_CONFIG_PATH
    return from_path


def configure(
    path: OptStrPath = None,
    host=None,
    port=None,
    overwrites: List[Tuple[str, str]] = None,
) -> None:
    """Using given arguments create a config that
    will be loaded anywhere in the program"""
    from_path = _find_config_path(path)
    yaml_dict = load_yaml(from_path)

    # Edit yaml
    conf = config_from_dict(yaml_dict)
    host_setter = functools.partial(conf.server.__setattr__, "host")
    port_setter = functools.partial(conf.server.__setattr__, "port")
    _set_if_value(host_setter, host)
    _set_if_value(port_setter, port, as_type=int)

    if overwrites:
        for overwrite in overwrites:
            key, value = overwrite
            if isinstance(value, str):
                value = f"'{value}'"
            try:
                exec(f"conf.{key} = {value}")
            except SyntaxError:
                print(f"Invalid replacement: {key!r} = {value!r}")

    # Write to work config
    create_work_config(conf)
