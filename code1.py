"""
Module docstring
"""

import sys

def exit_program():
    """
    This function prompts the user to enter 1 to continue or 0 to exit.
    """
    ex = 2
    while ex not in {1, 0}:  # using 'in' for comparison
        ex = int(input("Enter 1 to continue or 0 to exit: "))
    return ex

# Variable to keep track of loop iterations
COUNTER = 0

# Create variable for bool
STAY = True

while STAY:
    print(COUNTER)
    COUNTER += 1
    STAY = exit_program()

print("You have exited the loop")

