"""
Summary:
    Turn a list of values into a column for Sheets API
"""
from pprint import pprint


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    columns = [*zip(*[values])]
    pprint(columns)
