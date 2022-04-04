"""
Summary:
    Print documentation for all python modules in the current folder
Description:
    Simple script to get all docs from all modules
"""
import yaml
from pathlib import Path


if __name__ == "__main__":
    files = list(Path(".").glob("*.py"))
    for file in files:
        doc = __import__(file.stem).__doc__
        if doc:
            doc = yaml.safe_load(doc)
            print(doc)
