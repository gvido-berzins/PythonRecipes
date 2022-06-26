"""
Summary:
    Testing the speed of pathlib and os doing path operations
Description:
    Simple test of concatinating and creating a directory
"""
import os
import shutil
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WORK_DIR = SCRIPT_DIR / "workdir"
ITERATIONS = 100


def bench(name, func, iterations=ITERATIONS):
    print(f"Iteration: {name}")
    start_time = time.time()
    for _ in range(iterations):
        func()
    print(f"Took: {time.time()-start_time}s")


def pmakedirs():
    dir1 = str(time.time())
    dir2 = str(time.time())
    path = WORK_DIR.joinpath(dir1, dir2, dir2, dir1)
    path.mkdir(parents=True, exist_ok=True)


def osmakedirs():
    dir1 = str(time.time())
    dir2 = str(time.time())
    path = os.path.join(WORK_DIR, dir1, dir2, dir2, dir1)
    os.makedirs(path, exist_ok=True)


def run_benchmarks():
    name = "pathlib makedirs"
    bench(name, pmakedirs)

    name = "os makedirs"
    bench(name, osmakedirs)


if __name__ == "__main__":
    shutil.rmtree(WORK_DIR)
    WORK_DIR.mkdir(exist_ok=True)

    run_benchmarks()
