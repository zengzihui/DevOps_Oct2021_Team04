from classes.menu import *


def main():
    first_time_display_menu = False

    # default city size
    city_size = [4, 4]

    while True:
        chosen_option = main_menu(first_time_display_menu)
        first_time_display_menu = True
        if chosen_option == "0":
            exit_game()
        elif chosen_option == "1":
            start_new_game(width=city_size[0], height=city_size[1])
        elif chosen_option == "3":
            Game(city_size[0],city_size[1]).display_high_score() 
        elif chosen_option == "5":
            city_size = prompt_city_size(city_size)


if __name__ == "__main__":
    main()
