"""
Summary:
    Testing the lambda function in filter and sorting
"""
import re


def main():
    list_ = ["test1", "test2", "test0", None, ""]
    filtered_list = list(filter(lambda x: isinstance(x, str) and x, list_))
    sorted_list = sorted(
        list(filtered_list), key=lambda x: re.search(r"test(\d{1,2})", str(x)).group(1)
    )
    print(list(filtered_list))
    print(sorted_list)


if __name__ == "__main__":
    main()
