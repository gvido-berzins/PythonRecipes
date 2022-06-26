#!/usr/bin/python3
"""
Summary:
    Task scheduler to send a request to a Flask endpoint
Description:
    Using APScheduler schedule a task/function to execute on
    a specific interval, in this case, a function that sends
    POST requests to a local flask endpoint.
Credits:
    - https://stackoverflow.com/questions/21214270/how-to-schedule-a-function-to-run-every-hour-on-flask
"""

import json
import logging
import time
from pathlib import Path

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, abort, jsonify, request

logfile = "log.txt"
logger = logging.getLogger()
file_handler = logging.FileHandler(logfile, mode="w")
stream_handler = logging.StreamHandler()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

schedule_msg = "Scheduler is alive!"


app = Flask(__name__)


@app.route("/send", methods=["POST"])
def send():
    """Receives and logs a post request"""
    data = request.get_json()
    try:
        param = data["param"]
    except:
        return abort(403)

    if request.method == "POST" and param:
        logger.info(f"{schedule_msg} -> {param}")
    return jsonify({"Status": "OK"})


@app.route("/")
def index():
    """Homepage to count received scheduler tasks"""
    times_called = Path(logfile).read_text().count(schedule_msg)
    return f"Function called {times_called} times"


def send_task(param):
    """Scheduled task to send a post request"""
    headers = {"Content-Type": "application/json"}
    url = "http://127.0.0.1:8001/send"
    data = json.dumps({"param": f"{param}"})
    requests.post(url, data=data, headers=headers)


def init_scheduler(task: callable, args: tuple = None, interval=(0, 0, 1)):
    """Initializes the a scheduled task"""
    hours, minutes, seconds = interval
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(
        task, "interval", hours=hours, minutes=minutes, seconds=seconds, args=args
    )
    sched.start()


if __name__ == "__main__":
    init_scheduler(task=send_task, args=(time.time(),), interval=(0, 1, 0))
    app.run(debug=True, host="127.0.0.1", port=8001)
