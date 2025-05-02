# LoftCODE.py

from utils import handle_user_choice

def main():
    ex = 2
    print("Welcome to the program!")
    print("You can enter '1' to exit the program or '0' to continue the program.")

    while ex not in (0, 1):
        user_input = input("\nPlease enter your choice (1 to exit, 0 to continue): ")

        if user_input.isdigit():
            ex = int(user_input)
            handle_user_choice(ex)
        else:
            print("Error: Invalid input. Please enter a valid number (1 to exit, 0 to continue).")

def perform_task():
    """
    Simulates performing a task in the program after the user chooses to continue.
    This function could be expanded to include more complex logic, database interactions, or other features.
    """
    print("\nStarting a new task...")

    task_choice = 0
    while task_choice != 3:
        print("\nPlease select a task to perform:")
        print("1. Show current time")
        print("2. Display system information")
        print("3. Exit to main menu")
        
        try:
            task_choice = int(input("\nEnter your choice (1-3): "))
            
            if task_choice == 1:
                show_current_time()
            elif task_choice == 2:
                show_system_info()
            elif task_choice == 3:
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1-3).")

def show_current_time():
    """
    Displays the current date and time.
    """
    from datetime import datetime
    current_time = datetime.now()
    print(f"\nCurrent Date and Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

def show_system_info():
    """
    Displays basic system information (for example, Python version, platform).
    """
    import platform
    import sys

    print("\nSystem Information:")
    print(f"Operating System: {platform.system()} {platform.version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Python Version: {sys.version}")

def log_action(action_code):
    """
    Logs the user's action (exit or continue) into a file for tracking purposes.
    This function creates a log file if it doesn't exist, and appends the action to it.
    """
    import os
    log_filename = "program_log.txt"
    
    # Ensure the log file exists or create one
    if not os.path.exists(log_filename):
        with open(log_filename, "w") as log_file:
            log_file.write("Program Log Initialized.\n")

    # Open or create a log file (if not already present)
    with open(log_filename, "a") as log_file:
        # Log the action with a timestamp for clarity
        timestamp = get_timestamp()
        if action_code == 1:
            log_file.write(f"Exiting the program: {timestamp}\n")
        elif action_code == 0:
            log_file.write(f"Continuing the program: {timestamp}\n")
        else:
            log_file.write(f"Invalid action code: {action_code} at {timestamp}\n")

def get_timestamp():
    """
    Returns the current date and time in a formatted string.
    This is used for logging purposes.
    """
    from datetime import datetime
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

# Start the program by calling the main function
if __name__ == "__main__":
    main()
