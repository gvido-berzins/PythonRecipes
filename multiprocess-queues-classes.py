from multiprocessing import Process, Queue, freeze_support


class JobExecutor:
    def __init__(self, channel: Queue):
        self.channel = channel

    def __call__(self, *args, **kwargs):
        self.channel.put("Joob Started!")


class Listener:
    def __init__(self, channel: Queue):
        self.channel = channel

    def __call__(self, *args, **kwargs):

        while True:
            el = self.channel.get("Joob Started!")
            print(el)


def run():
    job_channel = Queue()
    job_executor = JobExecutor(job_channel)
    listener = Listener(job_channel)
    Process(target=job_executor).start()
    Process(target=listener).start()


if __name__ == "__main__":
    freeze_support()
    run()
