"""
Summary:
    Download a file with ftplib from standart library
"""
import ftplib
from pathlib import Path


def main():
    netloc = "ftp.vim.org"
    port = 21
    local_path = Path("/tmp/robots.txt")
    remote_path = "pub/robots.txt"

    with ftplib.FTP() as ftp:
        print("CONNECTING".center(70, "-"))
        res = ftp.connect(host=netloc, port=port)
        ftp.debug(2)
        ftp.login()

        print("CHECKING CWD".center(70, "-"))
        res = ftp.dir()
        print(res)
        print(f"DOWNLOADING {remote_path}".center(70, "-"))
        with local_path.open("wb") as f:
            ftp.retrbinary(f"RETR {remote_path}", f.write)

        print("LISTING FILE CONTENTS".center(70, "-"))
        print(local_path.read_text())


if __name__ == "__main__":
    main()
