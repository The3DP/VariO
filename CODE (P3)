def exit_program():
    """
    This function manages the user interaction for exiting or continuing the program.
    The user can input 1 to exit, 0 to continue, or any invalid input to prompt the user for correct input.
    """
    
    # Initialize variable 'ex' with a value other than 1 or 0 to start the loop
    ex = 2  
    
    print("Welcome to the program!")
    print("This function allows you to either continue or exit the program.")
    print("You can enter '1' to exit the program or '0' to continue the program.")
    
    # Start a loop that will continue until the user enters either '1' or '0'
    while ex != 1 and ex != 0:
        try:
            # Prompt the user for input
            user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")
            
            # Check if the input is a digit (i.e., an integer string)
            if user_input.isdigit():
                ex = int(user_input)  # Convert the input string to an integer
            else:
                # If input is not a digit, prompt the user for a valid input
                print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")
            
            # Display different messages depending on the input
            if ex == 1:
                print("\nYou have chosen to exit the program. Goodbye!")
            elif ex == 0:
                print("\nYou have chosen to continue. The program will continue running.")
            else:
                print("Error: Input out of expected range. Please enter only 1 or 0.")
                
        except ValueError:
            # If there's any error during input (though unlikely with 'isdigit' check)
            print("Error: Something went wrong while processing your input. Please try again.")
    
    # Additional behavior after exiting or continuing
    # Here, we simulate a program performing additional actions based on the user's choice
    if ex == 1:
        print("Exiting the program... Saving progress and shutting down.")
        # You could add code here to save data or clean up resources if needed
    elif ex == 0:
        print("Continuing the program... Performing the next task.")
        # Code for continuing the program goes here
        # You might want to call other functions or perform other logic in the program

    # Log action (whether the user exited or continued) for debugging or tracking purposes
    log_action(ex)


def log_action(action_code):
    """
    Logs the user's action (exit or continue) into a file for tracking purposes.
    This function creates a log file if it doesn't exist, and appends the action to it.
    """
    # Open or create a log file (if not already present)
    with open("program_log.txt", "a") as log_file:
        # Log the action with a timestamp for clarity
        if action_code == 1:
            log_file.write(f"Exiting the program: {get_timestamp()}\n")
        elif action_code == 0:
            log_file.write(f"Continuing the program: {get_timestamp()}\n")
        else:
            log_file.write(f"Invalid action code: {action_code} at {get_timestamp()}\n")


def get_timestamp():
    """
    Returns the current date and time in a formatted string.
    This is used for logging purposes.
    """
    from datetime import datetime
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


# Start the program by calling the exit_program function
if __name__ == "__main__":
    exit_program()

