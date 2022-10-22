"""
Oct 2022.

Potential solutions to questions in hello.py

@author ⤳ Valere Lambert & Travis Alongi
"""

from datetime import datetime


def hello():
    """Print  "Hello World" and return None."""
    print("Hello World")


# Main call of function
hello()

# Things to consider implements:
# 1) pass a string to the hello function (like a name) to print after "hello"


def hello(name):
    """Print  "Hello  <name>"" and return None."""
    print("Hello  %s" % name)


hello('Gandalf')

# 2) implement a check to see if the string is a proper name and if not,
#    request a new string


def hello(name):
    """Simple definition to print "Hello  <name> if a real name."""
    if type(name) == str:
        print("Hello  %s" % name.capitalize())
    else:
        print("The value you entered is not a string or is too short")
        print(" - try again")
        name = input('Input a name ...')
        print("Hello  %s" % name.capitalize())


# 3) Add a birth year to calculate the user's name and return it


def hello(name, birth_year):
    if type(name) == str:
        print("Hello : %s was born in %s" %
              (name.capitalize(), str(birth_year)))
        return str(name), int(birth_year)
    else:
        print("Value entered is either not a string or is too short - try again")
        name = input('Input a name ')
        print("Hello : %s was born in %s" %
              (name.capitalize(), str(birth_year)))
        return str(name), int(birth_year)


# 4) Store the users name and age in a variable as a tuple and write a new
#    function that then calculates the year that the user will turn 21 or the
#    year that user turned 21, use print to return a sensible message.

name_bday = hello('Ricky', 2010)


def check_if_21(year_born):
    """Check if 21 years old.

    bugs galore, but does the job
    """
    date = datetime.now()
    age = date.year - year_born

    if age <= 0:
        print('Age entered is invalid')
    elif age >= 21:
        print('Over 21')
    else:
        print('Under 21')


check_if_21(name_bday[1])
