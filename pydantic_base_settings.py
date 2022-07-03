"""
Summary: Configuration using pydantic BaseSettings
Description:
    Using pydantic BaseSettings setup configuration from environment variables,
    configuration file and initializer.
"""
import os
from typing import Any, Dict, Tuple

import yaml
from pydantic import BaseSettings, Field
from pydantic.env_settings import SettingsSourceCallable

SETTINGS_FILENAME = "settings.yaml"


def load_settings(settings: BaseSettings, filename=SETTINGS_FILENAME) -> Dict[Any, Any]:
    with open(filename) as f:
        return yaml.safe_load(f)


def dump_settings(data: dict[Any, Any], filename=SETTINGS_FILENAME) -> None:
    with open(filename, "w") as f:
        yaml.safe_dump(data, f)


class DatabaseSettings(BaseSettings):
    url: str
    name: str
    username: str = "guest"
    password: str = "guest"

    class Config:
        env_prefix = "dbt_"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> Tuple[SettingsSourceCallable, ...]:
            """Add load from yml file, change priority and remove file secret option.
            Precendence is based on the return order."""
            return init_settings, env_settings, load_settings


def main() -> int:
    os.environ["dbt_url"] = "mongodb://prod/"
    dump_settings({"name": "test", "url": "mongodb://..."})

    settings = DatabaseSettings()
    os.remove(SETTINGS_FILENAME)
    print(settings)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
