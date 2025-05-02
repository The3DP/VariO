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
