"""
Summary:
    Getting only the exception from a traceback
"""
import traceback


def main():
    try:
        raise ValueError("Wut?")
    except ValueError as e:
        value = traceback.format_exception_only(e)
        print(value)


if __name__ == "__main__":
    main()
