import time
from multiprocessing import Process, Queue


def do_work(jobs, results):
    job_id, metric = jobs.get()
    print("processing: ", job_id, metric)
    time.sleep(2)
    results.put("1")


def main() -> int:
    jobs = Queue()
    results = Queue()
    jobs.put(("555", "fps"))
    do_work(jobs, results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
