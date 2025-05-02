def handle_user_choice(ex):
    if ex == 1:
        print("\nYou have chosen to exit the program. Goodbye!")
    elif ex == 0:
        print("\nYou have chosen to continue. The program will continue running.")
    else:
        print("Error: Input out of expected range. Please enter only 1 or 0.")

def exit_program():
    """
    This function prompts the user to enter 1 to exit or 0 to continue.
    """
    ex = 2  # Initialize a value that doesn't match the exit conditions
    while ex not in {1, 0}:  # using 'in' for comparison
        user_input = input("Enter 1 to exit or 0 to continue: ")  # Ask the user to input either 1 or 0

        # Validate the user input to make sure it's an integer
        if user_input.isdigit():
            ex = int(user_input)  # Convert the input to an integer
            handle_user_choice(ex)
        else:
            print("Invalid input. Please enter 1 or 0.")

if __name__ == "__main__":
    exit_program()
