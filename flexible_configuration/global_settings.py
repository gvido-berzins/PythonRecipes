from pathlib import Path

MODULE_DIR = Path(__file__).parent
CONFIG_DIR = MODULE_DIR / "configuration"
DEFAULT_CONFIG_PATH = CONFIG_DIR / "stage.server.yml"
WORK_CONFIG_PATH = MODULE_DIR / "server.config.yml"

GET_ENDPOINTS = ["/users"]
POST_ENDPOINTS = ["/users"]
DELETE_ENDPOINTS = []
PUT_ENDPOINTS = []
