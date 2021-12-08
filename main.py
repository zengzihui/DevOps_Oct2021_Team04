from classes.menu import *


def main():
    while True:
        chosen_option = main_menu()
        if chosen_option == "0":
            exit_game()


if __name__ == "__main__":
    main()
