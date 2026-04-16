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
                print(" View Reviews by Park")
            elif data_choice == "B":
                print(" View Reviews by Country")
            else:
                print("Return Main Menu")

    elif choice == "B":
        print("Visualise Data"),
    else:
        print("Exit"),
        break
