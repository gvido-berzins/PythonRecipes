"""
Summary:
    Example of a global variable with increment function
"""


def inc():
    global counter
    try:
        counter += 1
    except NameError:
        counter = 1
    return counter


def main():
    # First initialize the variable
    # Access the variable
    # Increment the global variable
    inc()
    inc()
    inc()
    inc()
    inc()
    global counter
    print(counter)


if __name__ == "__main__":
    main()
