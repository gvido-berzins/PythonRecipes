"""
Summary:
    PoC Script runner Script with virtualenvironment setup
Description:
    Overcomplicated script with setting up the dummy data processing
    script and deleting it using a context manager.
    PoC part is on the command_list and Popen line.
"""
import shutil
from pathlib import Path
from subprocess import STDOUT, Popen

MODULE_DIR = Path(__file__).parent


class ScriptSetupEnv:
    """Class that represents a script environment, that is responsible
    for setup and teardown"""

    def __init__(self, metric_dir: Path, metric_script_path: Path):
        self.script_dir = metric_dir
        self.script_path = metric_script_path

    def __enter__(self):
        """ "Create" a script"""
        self.script_dir.mkdir(exist_ok=True)
        self.script_path.write_text(
            """import sys
import time
path = sys.path[1]
print(f"Processing data: {path}")
for _ in range(5):
    print("[*] Processing...")
    time.sleep(1)
print("DONE!")"""
        )
        requirements_txt_path = self.script_dir / "requirements.txt"
        requirements_txt_path.write_text(
            """requests
python-dotenv"""
        )

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            input(f"Press enter to remove: {self.script_dir} (to exit CTRL+C)")
            shutil.rmtree(self.script_dir)
        except KeyboardInterrupt:
            ...
        print()
        print("🥳 \u001b[34mDONE!\u001b[0m 🥳")


def run():
    metric_dir = MODULE_DIR / "some_metric"
    metric_script = "process.py"
    metric_script_path = metric_dir / metric_script

    # Commands
    metric_command = f"python {metric_script} path/to/file/video.mkv"
    command_list = [
        "pwd",  # Check current path
        "ls -la",  # Check current directory
        "python -m venv venv",  # Create virtual environment
        "source venv/bin/activate",  # Activate environment
        "python -m pip install -r requirements.txt",
        "pip list",  # Check installed packages
        "which python",  # Check current interpreter location
        metric_command,
    ]
    print()
    print("Command execution order:")
    for i, l in enumerate(command_list, start=1):
        print(f"{i}. '{l}'")

    # To run multiple commands in the terminal, separate them with semicolon
    full_command_string = ";".join(command_list)

    # The PoC starts here
    with ScriptSetupEnv(metric_dir, metric_script_path):
        print()
        print("🪄 \u001b[32mStarting Metric Script!\u001b[0m 🪄")
        # shell - create a terminal session
        # cwd - change working directory
        # stderr - show errors on output
        process = Popen(full_command_string, shell=True, cwd=metric_dir, stderr=STDOUT)
        print("-" * 10)

        # Wait for process to finish and print output, line by line
        for line in process.communicate():
            if line:
                print(line)

        print("=" * 10)


if __name__ == "__main__":
    run()
