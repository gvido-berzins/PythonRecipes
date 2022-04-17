"""
Summary:
    Convert a vmdk vmware image to qcow2 image
Description:
    Must have `qemu-img` qemu cli tool (sudo apt install qemu)
CLI:
    qemu-img convert image.vmdk -O qcow2 image.qcow2
"""
import shlex
import subprocess
import sys
from pathlib import Path


def vmdk_to_qcow(path: Path):
    outpath = path.parent
    new_path = outpath / f"{path.stem}.qcow2"
    cmd = f"qemu-img convert {path} -O qcow2 {new_path}"
    ret = subprocess.call(shlex.split(cmd))
    if ret == 1:
        print("Failed to convert file. Make sure the file exists or you have permissions")
        sys.exit(1)
    return new_path


def str_to_path(path: str) -> Path:
    return Path(path.replace(" ", "\\ ")).resolve()


def main():
    path = str_to_path("64bit/Linux Lite 5.8 (64bit).vmdk")
    path = vmdk_to_qcow(path)
    print(f"New Path: {path}")


if __name__ == "__main__":
    main()
