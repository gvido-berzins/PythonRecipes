"""
Summary:
    Sort a list of filenames, with using one or 3 keys
"""
import re

TEST_NUMBER_REGEX = re.compile(r"test(?:(\d{1,2})_(\d{1,3}))")
test_data = [
    "sometest-of-file-test2_0.txt",
    "sometest-of-file-test1_2.txt",
    "sometest-of-file-test3_20.txt",
    "sometest-of-file-test2_20.txt",
    "sometest-of-file-test1_1.txt",
    "sometest-of-file-test2_10.txt",
    "sometest-of-file-test1_21.txt",
    "sometest-of-file-test15_1.txt",
    "sometest-of-file-test1_21.txt",
    "sometest-of-file-test15_5.txt",
    "Some unsupported file.txt",
]

def tprint(*args, **kwargs):
    print(args, kwargs, "<br>")


def two_number_sort(filename):
    try:
        match = TEST_NUMBER_REGEX.search(filename)
        return int(match.group(1)), int(match.group(2))
    except (AttributeError, ValueError):
        return 0, 0


def four_whatever_sort(filename):
    try:
        match = TEST_NUMBER_REGEX.search(filename)
        return int(match.group(1)), int(match.group(2)), len(filename), ord(filename[0])
    except (AttributeError, ValueError):
        return 0, 0, 0, 0


def printl(list_):
    for el in list_:
        print(el)


def main():
    sorted_files = sorted(test_data, key=two_number_sort)
    print("~> Two number sort")
    printl(sorted_files)
    print()

    print("~> Some other 4 key sort")
    sorted_files = sorted(test_data, key=four_whatever_sort)
    printl(sorted_files)


if __name__ == "__main__":
    main()
