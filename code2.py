def exit():
    ex = 2  # Initialize a value that doesn't match the exit conditions
    while ex != 1 and ex != 0:
        # Ask the user to input either 1 or 0
        user_input = input("Enter 1 to exit or 0 to continue: ")
        
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

