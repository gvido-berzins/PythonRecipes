"""
Summary:
    Global variables
Description:
    Testing how global variables work within
    different scopes.
"""
global variable
variable = None


def fun_will_not_change_global():
    """Variable is in the local scope"""
    variable = "CHANGED FROM FUNCTION 1"


def fun_will_change_global():
    """Global variable is referenced"""
    global variable
    print(f"Global before change: {variable=}")
    variable = "CHANGED FROM FUNCTION 2"


def fun_succeeds():
    """Will print the global variable"""
    print(variable)


def fun_will_fail():
    try:
        print(variable)
        variable = 1
    except UnboundLocalError:
        print("Fails when referencing the global variable")


if __name__ == "__main__":
    fun_will_not_change_global()
    print(variable)

    fun_will_change_global()
    print(variable)

    fun_succeeds()

    fun_will_fail()
