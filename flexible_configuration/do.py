"""Accessing the generated configuration by running `main` first"""
try:
    from . import config
except ImportError:
    import config


def start():
    config_obj = config.get_config()
    print(config_obj)
