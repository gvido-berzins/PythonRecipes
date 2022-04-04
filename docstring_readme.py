"""
Summary:
    Script for grabbing all module docstrings and creating a readme section
Description:
    I wanted to utilize the docstrings in my Python Recipe GitHub repo, thus
    this script.
"""
from copy import copy
from pathlib import Path

import yaml


def append_sub_section(name: str, description: str, content: str) -> None:
    if value := description.get(name):
        return f"#### {name}\n\n{value}\n\n"
    return ""


def prepare_readme_section(header, description: dict) -> str:
    header = f"### `{header}`\n\n"
    section = copy(header)
    section += append_sub_section("Summary", description, section)
    section += append_sub_section("Description", description, section)
    section += append_sub_section("References", description, section)
    if header == section:
        return ""
    return section


if __name__ == "__main__":
    files = list(Path(".").glob("*.py"))
    content = ""
    for file in files:
        doc = __import__(file.stem).__doc__
        if doc:
            doc = yaml.safe_load(doc)
            section = prepare_readme_section(file.name, doc)
            content += section

    Path("readme_result.txt").write_text(content)
    print("Done")
