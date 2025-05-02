"""
Module docstring
"""

import sys

def main():
    ex = 2
    print("Welcome to the program!")
    print("You can enter '1' to exit the program or '0' to continue the program.")

    while ex not in (0, 1):
        user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")

        if user_input.isdigit():
            ex = int(user_input)
            if ex == 1:
                print("\nYou have chosen to exit the program. Goodbye!")
            elif ex == 0:
                print("\nYou have chosen to continue. The program will continue running.")
            else:
                print("Error: Input out of expected range. Please enter only 1 or 0.")
        else:
            print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")

# Variable to keep track of loop iterations
COUNTER = 0

# Create variable for bool
STAY = True

while STAY:
    print(COUNTER)
    COUNTER += 1
    STAY = exit_program()

print("You have exited the loop")

