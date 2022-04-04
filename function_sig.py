#!/usr/bin/env python3.10
"""
Summary:
    Print a function signature for give callable
"""
from dataclasses import dataclass
from inspect import signature


@dataclass
class Job:
    id: str
    pid: str


def execute_job(job: Job, delay: int | float = 0.1) -> str:
    return "PID: 9001"


if __name__ == "__main__":
    print(signature(execute_job, follow_wrapped=True))
