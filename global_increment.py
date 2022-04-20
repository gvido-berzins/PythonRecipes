def inc():
    global variable
    variable += 1


def init():
    global variable
    variable = 0


# First initialize the variable
init()

# Access the variable
global variable
print(variable)

# Increment the global variable
inc()
inc()
inc()
print(variable)
