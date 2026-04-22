"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import tui
tui.display_header()

import process
dataset = process.process_data()

while True:
    print("")
    choice = tui.get_menu_choice()

    if choice == "A":
            tui.display_data(dataset)
            data_choice = tui.get_data_choice()
            if data_choice == "A":
                park_counts = process.get_reviews_by_park(dataset)
                tui.display_reviews_by_park(park_counts)

            elif data_choice == "B":
                country_counts = process.get_ratings_by_country(dataset)
                tui.display_ratings_by_country(country_counts)

            elif data_choice == "C":
                pass

            else:
                print("Return Main Menu")

    elif choice == "B":
        print("Visualise Data"),
    else:
        print("Exit"),
        break

