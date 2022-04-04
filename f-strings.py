"""
Summary:
    Cheatsheet for f-strings (Just because I keep forgetting how to use them)
Description:
    Ways to use the f-string to perform more than interpolating variables, which
    includes substitution, raw printing, padding and formatting decimals.
"""
from random import randint

num = 1.99
raw = b"Raw bytes"
string = "I am a string"
int_list = [randint(1, 6) for _ in range(5)]

big_f = f"""
# Introduction to f-strings!

## Basics

This is a regular num variable:
{num}

With a bit of verbosity using '=' sign
{num=}

Let's show raw energy:
{raw!r}

## Formatting numbers

Formatting it now to decimals
{num:.0100f}

Percentage?
{num:.01%}

## Let's add padding so our logs look good

Padding is the amount of spaces from the left side to the right

No not this:
{"Line: " + str(randint(10000000, 1000000000))} Info log
{"Line: " + str(randint(1, 1999))} Error?

This looks better, doesn't it?
{"Line: " + str(randint(10000000, 1000000000)):40} Something happened?!
{"Line: " + str(randint(1, 1999)):40} False alarm

Need some space?
Yes, much appreciated. {1:6}, but only for the numbers
What about the string? {string:600}, the padding is afterwards?

Justification

{"my string":>30}
{"my string":>25}
{"my string":>20}
{"my string":>15}
{"my string":>10}

- Oh look a staircase!

## Formatting dates

A: What time is it?
B: Hey it's {__import__("datetime").datetime.now():%A %H:%M:%S}

## Some other numeric things

Hex {5555:x}
Octal {5555:o}
Sciecy {5555:e}
"""

if __name__ == "__main__":
    print(big_f)
