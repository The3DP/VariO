from utils import handle_user_choice, get_user_input

def main():
    print("Welcome to the program!")
    print("You can enter '1' to exit the program or '0' to continue the program.")
    ex = get_user_input()
    handle_user_choice(ex)

if __name__ == "__main__":
    main()
