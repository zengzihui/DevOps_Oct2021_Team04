from classes.menu import *


def main():
    building_pool = ["HSE","FAC","SHP","HWY","BCH"]
    first_time_display_menu = False

    # default city size
    city_size = [4, 4]

    while True:
        all_buildings = {}
        chosen_option = main_menu(first_time_display_menu)
        first_time_display_menu = True
        for building in building_pool:
            all_buildings[building] = 8

        if chosen_option == "0":
            exit_game()
        elif chosen_option == "1":
            start_new_game(width=city_size[0], height=city_size[1], building_pool= all_buildings)
        elif chosen_option == "4":
            temp_pool = choose_building_pool(building_pool)
            if temp_pool != None:
                building_pool = temp_pool
            else:
                print_building_display(building_pool)
        elif chosen_option == "5":
            city_size = prompt_city_size(city_size)


if __name__ == "__main__":
    main()
