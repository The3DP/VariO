"""
Module docstring
"""

def handle_user_input():
    """
    Handles user input for exiting or continuing the program.
    """
    while True:
        user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")
        if user_input.isdigit():
            choice = int(user_input)
            if choice in (0, 1):
                return choice
            print("Error: Input out of expected range. Please enter only 1 or 0.")
        else:
            print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")

def main():
    """
    Main function to start the program.
    """
    print("Welcome to the program!")
    print("You can enter '1' to exit the program or '0' to continue the program.")

    while True:
        user_choice = handle_user_input()
        if user_choice == 1:
            print("\nYou have chosen to exit the program. Goodbye!")
            break
        print("\nYou have chosen to continue. The program will continue running.")

if __name__ == "__main__":
    main()
