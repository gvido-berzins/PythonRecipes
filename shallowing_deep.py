"""
Summary:
    Testing the difference between shallow and deep copy
"""
from copy import copy, deepcopy


def main():
    nested_wutt = ["wutt"]
    wut = ["wut", nested_wutt]
    wut_copy = copy(wut)
    wut_deepcopy = deepcopy(wut)

    wut.append("wutt")
    nested_wutt.append("nwutt")
    print("Original values:", wut)
    print("Shallow copy:", wut_copy)
    print("Deep copy:", wut_deepcopy)
    """
    ~> Results:
    Original values: ['wut', ['wutt', 'nwutt'], 'wutt']
    Shallow copy: ['wut', ['wutt', 'nwutt']]
    Deep copy: ['wut', ['wutt']]
    """


if __name__ == "__main__":
    main()
