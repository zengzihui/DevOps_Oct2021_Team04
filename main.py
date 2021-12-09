from classes.menu import *


def main():
    first_time_display_menu = False
    while True:
        chosen_option = main_menu(first_time_display_menu)
        if chosen_option == "0":
            exit_game()
        elif chosen_option == "1":
            first_time_display_menu = True
            start_new_game()


if __name__ == "__main__":
    main()
