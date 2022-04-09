"""
Summary:
    A quick script using ipaddress module to ping all hosts in a network
Description:
    Uses multiprocessing to ping address more quickly by proving multiple networks.
    Change WORKER_COUNT for speed.
Example:
    $ python network-ping-ipaddress.py 192.168.122.0/24 192.168.41.0/24
"""
import ipaddress
import shlex
import subprocess
import sys
import time
from argparse import ArgumentParser
from multiprocessing import Process, Queue

WORKER_COUNT = 100


def network_type(targets) -> list[ipaddress.IPv4Network]:
    return ipaddress.IPv4Network(targets)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("targets", type=network_type, nargs="+", help="Target network")
    return parser.parse_args()


def worker(queue: Queue):
    while True:
        host = queue.get()
        command = shlex.split(f"ping -c 1 -w 1 {host}")
        ret = subprocess.call(command, stdout=subprocess.DEVNULL)
        if ret == 0:
            print(host, "active")
        if queue.empty():
            break
    sys.exit(0)


def generate_queue(queue: Queue, targets: list[ipaddress.IPv4Network]):
    for target in targets:
        for host in target.hosts():
            queue.put(host)


def main():
    print(args.targets)
    processes = []
    queue = Queue()
    generate_queue(queue, args.targets)
    for _ in range(WORKER_COUNT):
        process = Process(target=worker, args=(queue,))
        process.start()
        processes.append(process)

    for p in processes:
        p.join()


if __name__ == "__main__":
    started = time.time()
    args = parse_args()
    main()
    finished = time.time()
    print(f"Time taken: {finished - started}s")
