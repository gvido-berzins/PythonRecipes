"""
Summary:
    Get all IP addresses from a string using regex.
"""
import re
from pprint import pprint


def main():
    a = """
    1- 172.16.226.9
    2- 172.16.228.6
    3- 172.16.230.11 (ChromeBook i3)
    4- 172.16.220.6
    5- 172.16.221.10
    6- 172.16.222.7 (ChromeBook)
    """

    IP_REGEX = re.compile(r"((\d{1,3}\.\d{1,3}\.\d{1,3})\.\d{1,3})")
    # IP_REGEX = re.compile(r"((?:[0-9]{1,3}\.){3}[0-9]{1,3})")

    al = IP_REGEX.findall(a)

    # All groups
    pprint(al)

    # A set of the first 3 octets
    # al = {ip for _, ip in al}
    pprint(al)


if __name__ == "__main__":
    main()
