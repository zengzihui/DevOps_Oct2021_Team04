from classes.menu import *


def main():
    building_pool = ["BCH", "FAC", "HSE", "SHP", "HWY"]
    first_time_display_menu = False
    while True:
        chosen_option = main_menu(first_time_display_menu)
        if chosen_option == "0":
            exit_game()
        elif chosen_option == "1":
            first_time_display_menu = True
            start_new_game()
        elif chosen_option == "4":
            first_time_display_menu = True
            temp_pool = choose_building_pool()
            if temp_pool != None:
                building_pool = temp_pool
            else:
                print_building_display(building_pool)

if __name__ == "__main__":
    main()
