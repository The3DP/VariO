"""
Module docstring
"""

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
        # Validate the user input to make sure it's an integer
        if user_input.isdigit():
            ex = int(user_input)  # Convert the input to an integer
        else:
            print("Invalid input. Please enter 1 or 0.")
    
    # Provide feedback based on the user's choice
    if ex == 1:
        print("Exiting the program.")
    elif ex == 0:
        print("Continuing the program.")

# Example usage
if __name__ == "__main__":
    exit_program()

