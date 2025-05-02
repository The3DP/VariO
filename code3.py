from utils import handle_user_choice, get_user_input

def main():
    print("Greetings! Let's get started.")
    print("Type '1' to quit or '0' to proceed.")
    ex = get_user_input()
    handle_user_choice(ex)

if __name__ == "__main__":
    main()
