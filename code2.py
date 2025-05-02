from utils import handle_user_choice, get_user_input

def main():
    print("Hello! This is another part of the program.")
    print("You can enter '1' to exit or '0' to stay.")
    ex = get_user_input()
    handle_user_choice(ex)

if __name__ == "__main__":
    main()
