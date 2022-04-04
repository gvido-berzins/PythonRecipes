"""
Summary:
    pathlib Path object operations
Description:
    Showing the same operations that can be done with os module,
    instead using pathlib module
Full correspondence table is available in the docs:
- https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module
"""
from pathlib import Path

# Defining the current MODULE directory
SCRIPT_DIR = Path(__file__).parent


def start():
    # Getting the current working directory
    cwd = Path().resolve()
    cwd = Path(".").resolve()
    cwd = Path("./").resolve()
    print(f"CWD is '{cwd}'")

    # Concatinating a path
    work_dir = SCRIPT_DIR / "workdir"
    nested_dir = work_dir.joinpath("deep", "in", "the", "nest")

    # Making directories (single and nested)
    work_dir.mkdir(exist_ok=True)
    nested_dir.mkdir(exist_ok=True, parents=True)

    # Writing to a file
    file_path = work_dir / "somefile.txt"
    file_path.write_bytes(b"Writting some bytes")
    file_path.write_text("This will overwrite existing contents\n")

    # Appending to a file
    with file_path.open("a") as f:
        f.write("Appending more to the file")

    # Reading from files
    content = file_path.read_text()
    print("\nPrinting file content...")
    print("---")
    print(content)
    print("---")

    # Removing files
    file_path.unlink(missing_ok=True)

    # Checking the existance
    exists = file_path.exists()
    is_dir = work_dir.is_dir()
    is_file = work_dir.is_file()
    print(
        f"""
    file_path.exists() = {exists}
    work_dir.is_dir() = {is_dir}
    work_dir.is_file() = {is_file}
    """
    )

    # Iterating over files/folders in a directory and printing stats
    root = Path("/")
    for f in root.glob("*"):
        stats = f.lstat()
        print(f"\n{f} stats:\n---")
        print(stats)

    # Going up a directory
    l1 = file_path.parent
    l2 = file_path.parent.parent
    lnum = 5
    nnum = (file_path / ("../" * lnum)).resolve()
    print(f"Whats above '{file_path}'?")
    print(f"L1: '{l1}'")
    print(f"L2: '{l2}'")
    print(f"L{lnum}: '{nnum}'")

    # Renaming files
    some_file = Path("./oldfile.txt")
    some_file.write_text(".")
    new_file = some_file.rename("coolername.txt")
    print(f"Cooler file exists: {new_file.exists()}")
    new_file.unlink()


if __name__ == "__main__":
    main()
