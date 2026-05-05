"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import tui
import process
import visual

tui.display_header()

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
                park_name = ""
                while True:
                    park_choice = tui.get_park_name()
                    if park_choice == "1":
                        park_name = "Disneyland_California"
                    elif park_choice == "2":
                        park_name = "Disneyland_Paris"
                    elif park_choice == "3":
                        park_name = "Disneyland_HongKong"
                    elif park_choice == "X":
                        break
                    else:
                        print("Invalid choice, please try again.")
                    if park_name != "":
                       country_name = tui.get_country_name()
                       reviews = process.get_reviews_by_park_and_country(dataset, park_name, country_name)
                       tui.display_reviews_by_park_and_country(len(reviews), park_name, country_name)

            elif data_choice == "C":
                park_months = process.get_park_months(dataset)
                tui.display_park_months(park_months)

            elif data_choice == "D":
                park_name = ""
                while True:
                    park_choice = tui.get_park_name()
                    if park_choice == "1":
                        park_name = "Disneyland_California"
                    elif park_choice == "2":
                        park_name = "Disneyland_Paris"
                    elif park_choice == "3":
                        park_name = "Disneyland_HongKong"

                    elif park_choice == "X":
                        break
                    else:
                        print("Invalid choice, please try again.")
                    if park_name != "":
                        year = tui.get_year()
                        avg = process.get_avg_ratings_by_park_and_year(dataset, park_name, year)
                        tui.display_avg_by_park_and_year(avg, park_name, year)

            elif data_choice == "X":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice, please try again.")

    elif choice == "B":
        while True :
            visual_choice = tui.get_visualise_choice().upper()

            if visual_choice == "A":
                park_reviews = process.get_reviews_by_park(dataset)
                visual.pie_chart_reviews_by_park(park_reviews)

            elif visual_choice == "B":
                park_name=""
                while True:
                    park_choice = tui.get_park_name()

                    if park_choice == "1":
                        park_name = "Disneyland_California"
                        break
                    elif park_choice == "2":
                        park_name = "Disneyland_Paris"
                        break
                    elif park_choice == "3":
                        park_name = "Disneyland_HongKong"
                        break

                    elif park_choice == "X":
                        break
                    else:
                        print("Invalid choice, please try again.")
                if park_name != "":
                    top_countries = process.get_avg_ratings_by_country_for_park(dataset, park_name)
                    visual.bar_chart_avg_by_country(top_countries)

            elif visual_choice == "C":
                park_name = ""
                while True:
                    park_choice = tui.get_park_name()
                    if park_choice == "1":
                       park_name = "Disneyland_California"
                       break
                    elif park_choice == "2":
                       park_name = "Disneyland_Paris"
                       break
                    elif park_choice == "3":
                       park_name = "Disneyland_HongKong"
                       break
                    elif park_choice == "X":
                       break
                    else:
                        print("Invalid choice, please try again.")
                    if park_name != "":
                        monthly_data = process.get_avg_ratings_by_month(dataset, park_name)
                        visual.bar_chart_avg_by_month(monthly_data)

                    elif visual_choice == "X":
                       print("Returning to main menu.")
                if park_name != "":
                     monthly_data = process.get_avg_ratings_by_month(dataset, park_name)
                     visual.bar_chart_avg_by_month(monthly_data)

    elif choice == "X":
        print("Goodbye!"),
        break
    else:
        print("Invalid choice, please try again.")


