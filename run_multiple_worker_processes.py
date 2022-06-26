"""
Summary:
    Run multiple worker processes and return status code
Description:
    A simple way to check what status code a main function returned
    when run with multiprocessing
"""
import multiprocessing as mp
import os
import random
import time
from typing import List, Tuple

ProcessStatus = Tuple[int, int, int]


def main() -> int:
    pid = os.getpid()
    for i in range(0, 5):
        time.sleep(0.8)
        print(f"[PID-{pid}] Running iteration {i}")
        exit_code = random.randint(0, 10)
        if exit_code % 3 == 0:
            return exit_code
    return 0


def run_worker(worker_num: int) -> ProcessStatus:
    """Wrapper for main function"""
    pid = os.getpid()
    print(f"Worker {worker_num} started on PID {pid}")
    ret = main()
    return worker_num, pid, ret


def get_failed_processes(process_statuses: List[ProcessStatus]) -> List[ProcessStatus]:
    failed = []
    for procnum, pid, code in process_statuses:
        if code != 0:
            failed.append((procnum, pid, code))
    return failed


def run_workers():
    workers = 5
    with mp.Pool(processes=workers) as pool:
        results = pool.map(run_worker, range(workers))
        print(f"Results: {results}")
        failed = get_failed_processes(results)
        if failed:
            for procnum, pid, code in failed:
                print(f"Process {procnum} with PID {pid} failed with code {code}")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run_workers())
