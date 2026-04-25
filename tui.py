"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
def display_header():
    print("--------------------------")
    print("Disneyland Review Analyser")
    print("--------------------------")
    print(" ")

def get_menu_choice():
    print()
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    choice = input("Please enter the letter which corresponds with your desired menu choice: ") .upper()
    return choice

def get_data_choice():
    print()
    print("[A] Most Reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")
    print("[X] Return to Main Menu")
    choice = input("Please enter the letter which corresponds with your desired menu choice: ") .upper()
    return choice

def display_reviews_by_park(park_counts):
    print()
    for row in park_counts:
        print(row[0], row[1])

def display_ratings_by_country(country_counts):
    print()
    for row in country_counts:
        print(row[0], row[1])

def display_park_months(park_months):
    print()
    for row in park_months:
        print(row)
        for month in park_months[row]:
            print(month, park_months[row][month])


def display_data(dataset):
    print(f"Dataset loaded: {(len(dataset))} reviews")