from pathlib import Path

from dynaconf import Dynaconf, Validator

MODULE_DIR = Path(__file__).parent
CONFIG_DIR = MODULE_DIR / "configs"

settings = Dynaconf(
    settings_files=[
        CONFIG_DIR / "default_settings.yaml",  # Ordering matters :)
        CONFIG_DIR / "settings.yaml",
        CONFIG_DIR / ".secrets.yaml",
    ],
    environments=True,
    load_dotenv=True,
    envvar_prefix="GNY",
    env_switcher="GNY_ENV",
    dotenv_path="configs/.env",
)

settings.validators.register(
    Validator("SERVER.HOST", must_exist=True, eq="10.10.10.2", env="test"),
    Validator("SERVER.HOST", must_exist=True, eq="10.10.10.111", env="stage"),
    Validator("SERVER.PORT", gte=9000, lte=10000, env="stage"),
    Validator("SERVER.PORT", gte=5000, lte=6000, env="test"),
    Validator("DB.USER", default="dbuser"),
    Validator("DB.PASSWORD", must_exist=True, when=Validator("DB.USER", must_exist=True)),
    Validator("DB.USER", ne="pgadmin") & Validator("DB.USER", ne="admin"),
)

settings.validators.validate()
