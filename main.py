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
tui.display_data(dataset)
while True:
    choice = tui.get_menu_choice()

    if choice == "A":
        while True:
            data_choice = tui.get_data_choice()
            if data_choice == "A":
                park_choice = tui.get_park_name()
                if park_choice == "1":
                    park_name = "Disneyland_California"
                elif park_choice == "2":
                    park_name = "Disneyland_Paris"
                elif park_choice == "3":
                    park_name = "Disneyland_HongKong"
                else:
                    print("Invalid choice, please try again.")
                    park_name = ""
                park_counts = process.get_park_reviews(dataset, park_name)
                tui.display_park_reviews(park_counts)

            elif data_choice == "B":
                while True:
                    park_choice = tui.get_park_name()
                    if park_choice == "1":
                        park_name = "Disneyland_California"
                    elif park_choice == "2":
                        park_name = "Disneyland_Paris"
                    elif park_choice == "3":
                        park_name = "Disneyland_HongKong"
                    else:
                        print("Invalid choice, please try again.")


                country_counts = process.get_ratings_by_country(dataset)
                tui.display_ratings_by_country(country_counts)

            elif data_choice == "C":
                park_months = process.get_park_months(dataset)
                tui.display_park_months(park_months)


            elif data_choice == "X":
                print("Returning to main menu.")
                break

            else:
                print("Invalid choice, please try again.")

    elif choice == "B":
        print("Visualise Data.")

    elif choice == "X":
        print("Goodbye!"),
        break
    else:
        print("Invalid choice, please try again.")


