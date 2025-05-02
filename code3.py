def handle_user_choice(ex):
    if ex == 1:
        print("\nYou have chosen to exit the program. Goodbye!")
    elif ex == 0:
        print("\nYou have chosen to continue. The program will continue running.")
    else:
        print("Error: Input out of expected range. Please enter only 1 or 0.")

def exit_program():
    """
    This function manages the user interaction for exiting or continuing the program.
    """
    ex = 2  # Initialize variable 'ex' with a value other than 1 or 0 to start the loop
    print("Welcome to the program!")
    print("You can enter '1' to exit the program or '0' to continue the program.")

    while ex not in (1, 0):
        user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")

        if user_input.isdigit():
            ex = int(user_input)
            handle_user_choice(ex)
        else:
            print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")

if __name__ == "__main__":
    exit_program()
