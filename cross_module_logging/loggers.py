import logging
from pathlib import Path


make_log = lambda x: f"{Path(__file__).stem}_{x}.txt"

top_logger = logging.getLogger("top")
handler = logging.FileHandler(make_log("top"), mode="a")
std_handler = logging.StreamHandler()
top_logger.addHandler(handler)
top_logger.addHandler(std_handler)
top_logger.setLevel(logging.DEBUG)

other_logger = logging.getLogger("other")
handler = logging.FileHandler(make_log("other"), mode="a")
std_handler = logging.StreamHandler()
other_logger.addHandler(handler)
other_logger.addHandler(std_handler)
other_logger.setLevel(logging.DEBUG)

