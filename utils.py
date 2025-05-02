# utils.py

def handle_user_choice(ex):
    """
    Handles the user's choice to exit or continue.
    """
    if ex == 1:
        print("\nYou have chosen to exit the program. Goodbye!")
    elif ex == 0:
        print("\nYou have chosen to continue. The program will continue running.")
    else:
        print("Error: Input out of expected range. Please enter only 1 or 0.")


def get_user_input():
    """
    Prompts the user for input until a valid choice is provided.
    """
    while True:
        user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")
