#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oct 2022.

Let's build on what we learned so far.
We'll work with functions, strings, itegers, booleans, etc.
to write code to do fun things and incrementally write code

Note: you may need to remove the first 2 lines of code for this to work
on your machine.

@author ⤳ Valere Lambert
"""

# Defining a function to request a string and pass to the hello function
def CallError():
    """
    Helper function for hello() function
    request a string from user commandline and pastt to hello function
    """
    new_str = input('Enter a string for name')
    hello(new_str)
    

# Define a function that takes a string input and prints "Hello" string
def hello(name):
    """Print  "Hello name" and return None.
    """
    
    # If the name is input is a string, print hello name
    if type(name) == str:
        newstring = "Hello "+(name)
        print(newstring)
    # If name is not a string, print an error and call the 
    # CallError function for new input
    else:
        print('Error in input please try again')
        CallError()



# Main call of function
hello("Fred")

