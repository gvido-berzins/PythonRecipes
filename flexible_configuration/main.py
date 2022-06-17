import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Tuple

from flexible_configuration.global_settings import CONFIG_DIR

try:
    from . import config
except ImportError:
    import config

SUPPORTED_EXTS = [".yml", ".yaml"]


def overwrite_type(arg: str) -> Tuple[str, str]:
    key, value = arg.split("=")
    return key, value


def path_type(path_str: str) -> Path:
    path = Path(path_str)
    if not path.exists():
        sys.exit(f"No such file exists: '{path}'")
    if path.suffix not in SUPPORTED_EXTS:
        sys.exit(f"Only {SUPPORTED_EXTS} extension is supported: '{path}'")
    return path


def env_type(env: str) -> Path:
    path = CONFIG_DIR / f"{env.lower()}.server.yml"
    if not path.exists():
        sys.exit(f"No configuration for environment: {env}")
    return path


def parse_args(args: list[str]):
    parser = ArgumentParser()
    parser.add_argument("--config", type=path_type)
    parser.add_argument("--env", type=env_type)
    parser.add_argument("--host", type=str, default=None)
    parser.add_argument("--port", type=int, default=None)
    parser.add_argument(
        "-o",
        action="extend",
        nargs="+",
        type=overwrite_type,
        help="Overwrites for the configuration",
    )
    return parser.parse_args(args)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    config_path = args.config or args.env
    config.configure(config_path, args.host, args.port, args.o)
    conf = config.get_config()
    print(conf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
