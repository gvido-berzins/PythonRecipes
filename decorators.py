import functools
from dataclasses import dataclass


def simple_dec(func):
    print("< Simple wrapper called >")
    return func


def fun_dec(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        ret = f"{args} {kwargs}"
        print("< Better wrapper called >")
        print(f'( I can see args : "{ret}" )')
        return func(*args, **kwargs)

    return inner


def arg_dec(x: int, y: float = 0.0, real: bool = False):
    print(f"< 2. Passed args to decorator: ({x=}, {y=}, {real=}) >")

    def fun_dec(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            ret = f"{args} {kwargs}"
            print("< 2. Argument wrapper called >")
            print(f'( 2. I can see args : "{ret}" )')
            return func(*args, **kwargs)

        return inner

    return fun_dec


def main():
    @simple_dec
    def ex1():
        """Using the simple decoreator to run a function"""

    @fun_dec
    def ex2(x: int, key: str = ""):
        """Using functools.wraps and being able to see arguments and keywordarguments"""

    @arg_dec(5)
    def ex3(w: bool):
        """Being able to pass arguments and keywork arguments to the decorator"""

    ex1()
    ex2(1, key="secret_key")
    ex3(True)


if __name__ == "__main__":
    main()
