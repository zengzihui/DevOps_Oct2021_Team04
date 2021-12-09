from classes.menu import *


def main():
    while True:
        chosen_option = main_menu()
        if chosen_option == "0":
            exit_game()
        elif chosen_option == "1":
            start_new_game()


if __name__ == "__main__":
    main()
