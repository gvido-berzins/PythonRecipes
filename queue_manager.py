from multiprocessing import Process, freeze_support, Queue
import time
import logging

root_logger = logging.getLogger(__name__)
processing_logger = logging.getLogger("processing")
cancellation_logger = logging.getLogger("cancellation")
queue_logger = logging.getLogger("queue")


class JobExecutor:
    def __init__(self, job_channel: Queue, status_channel: Queue):
        self.job_channel = job_channel
        self.status_channel = status_channel

    def __call__(self, *args, **kwargs):
        processing_logger.debug("Started")
        self.status_channel.put("Joob Started!")


class CancelListener:
    def __init__(self, job_channel: Queue, status_channel: Queue):
        self.job_channel = job_channel
        self.status_channel = status_channel

    def __call__(self, *args, **kwargs):
        cancellation_logger.debug("Started")
        while True:
            el = self.status_channel.get("Joob Started!")
            print(el)


class QueueManager:
    def __init__(self):
        self.processes = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        for p in self.processes:
            if not p.is_alive():
                p.terminate()

    def start_process(self, worker: callable, **kwargs):
        worker_obj = worker(**kwargs)
        process = Process(target=worker_obj)
        process.start()
        self.processes.append(process)
        time.sleep(1)


def main():
    with QueueManager() as qm:
        job_channel, status_channel = Queue(), Queue()
        qm.start_process(
            JobExecutor, job_channel=job_channel, status_channel=status_channel
        )
        qm.start_process(
            CancelListener, job_channel=job_channel, status_channel=status_channel
        )


if __name__ == "__main__":
    freeze_support()
    main()
