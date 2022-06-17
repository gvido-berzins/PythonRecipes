"""
Summary:
    Executing tasks in a different process and cancelling them saving task status
Description:
    A pattern to have a main process execute a job in a different process, later terminating
    the process and saving the task execution process using a SIGTERM signal handler
"""
import multiprocessing
import signal
import time
from dataclasses import dataclass, field


@dataclass
class Task:
    metric: str
    done: bool = False


@dataclass
class Job:
    id: str
    tasks: list[Task] = field(default_factory=list)
    done: bool = False


def do_work(q):
    job: Job = q.get()

    def put_back_job():
        q.put(job)

    signal.signal(signal.SIGTERM, put_back_job)

    try:
        print(f"+ Work started on job: {job.id}")
        for task in job.tasks:
            time.sleep(1)
            task.done = True
            print(f"+ task {task} done? {task.done}")
        job.done = True
    except:
        pass
    finally:
        put_back_job()
    print("+ Work finished")


def main() -> int:
    tasks = (
        Task("T1"),
        Task("T2"),
        Task("T3"),
    )
    job = Job("J#01", tasks)

    q = multiprocessing.Queue()
    print("Worker started".center(70, "-"))
    p = multiprocessing.Process(target=do_work, args=(q,))
    p.start()
    q.put(job)

    time.sleep(2.1)  # Wait for some tasks to finish
    p.terminate()
    job = q.get()

    task_statuses = [x.done for x in job.tasks]
    print(f"Job Done?: {job.done}")
    print(f"Tasks? {task_statuses}")
    print("end".center(70, "-"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
