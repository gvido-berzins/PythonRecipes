"""
Summary:
    Write new contents to files safely avoiding TOCTOU pattern
Description:
    Source: [atomic file replacement (os.rename vs os.replace) (interemdiate) anthony explains #264](https://www.youtube.com/watch?v=-9eXCb3yvyY)
"""
import os.path
import tempfile


def write_text(filename: str, content: str) -> None:
    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(filename))
    try:
        with open(fd, "w") as f:
            f.write(content)
        os.replace(tmp_path, filename)
    except BaseException:
        os.remove(tmp_path)


if __name__ == "__main__":
    write_text("file.txt", "Sup.")
