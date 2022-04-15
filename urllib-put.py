"""
Summary:
    Do a PUT request to a webdav server using urllib from standard library
"""
import urllib.request as ur
from pathlib import Path

FILE = "/etc/issue"
URL = "http://0.0.0.0:8001/res.txt"


def main():
    request = ur.Request(URL, Path(FILE).read_bytes(), method="PUT")
    response = ur.urlopen(request)
    print(response.status)


if __name__ == "__main__":
    main()
