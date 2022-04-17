"""
Summary:
    Monitor running processes, print new processes, monitor single process
Description:
    Implemented a few methods, check all running processes and print new additions to the
    list, monitor (and/or shutdown) a single process by name, find process by name
    (from docs)
References: |
    - [Few good samples in the official docs]()https://psutil.readthedocs.io/en/latest/#recipes)
"""
import curses
import textwrap
import time

import psutil


def check_running_processes(running_processes: list[psutil.Process]):
    for process in psutil.process_iter():
        if process not in running_processes:
            running_processes.append(process)
            print(f"New: {process.pid:>7} {process.name()}")


def start_listener(running_processes: list[psutil.Process], timeout=0.5):
    while True:
        check_running_processes(running_processes)
        time.sleep(timeout)


def monitor_process(name: str, timeout: int = 1) -> None:
    """Monitor a single process by its name"""
    screen = curses.initscr()
    while True:
        process = find_process_by_name(name)
        if process:
            children = [
                ", ".join([str(x.pid), x.name(), x.status()])
                for x in process.children(recursive=True)
            ]
            children = "\n".join(children)
            inf = f"""
            Name: {process.name()}
            User: {process.username()}
            Status: {process.status()}
            Parent: {process.parent()}

            Children:
            ---------
            """
            inf = textwrap.dedent(inf)
            screen.clear()
            screen.addstr(inf + children)
            screen.refresh()
            # process.terminate()
            # print(inf)
        time.sleep(timeout)


def find_process_by_name(name: str) -> psutil.Process:
    "Return a process matching 'name'"
    for p in psutil.process_iter(["name"]):
        if p.info["name"] == name:
            return p
    return None


def main():
    running_processes = []

    print("INITIAL CHECK".center(60, "-"))
    # check_running_processes(running_processes)
    print()

    print("MONITOR STARTED".center(60, "-"))
    # start_listener(running_processes)
    print()
    print("MONITORING SINGLE PROCESS".center(60, "-"))
    monitor_process("gcr-prompter")
    print()


if __name__ == "__main__":
    main()
