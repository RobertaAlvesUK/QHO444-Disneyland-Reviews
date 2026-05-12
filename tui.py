"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilize any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
def display_header():
    print("--------------------------")
    print("Disneyland Review Analyser")
    print("--------------------------")
    print(" ")

def display_data(dataset):
    print(f"Dataset loaded: {(len(dataset))} reviews")

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
        best_month = max(park_months[row], key=park_months[row].get)
        print("Best Month:", row, best_month)

def display_park_reviews(park_reviews):
    print()
    print(f"Total Reviews Found: {len(park_reviews)}")
    for row in park_reviews:
       print(f"Rating:{row[1]}, Date: {row[2]}, Location: {row[3]}")

def display_reviews_by_park_and_country(count, park_name, country_name):
    print(f"There are {count} reviews from {country_name} for {park_name}")

def display_avg_by_park_and_year(avg, park_name, year):
    print(f"The average rating for {park_name} in {year} is {avg}.")

def display_avg_ratings_by_park_and_country(results):
    print()
    for row in results:
        print(f"{row[0][0]} - {row[0][1]}: {row[1]}")



def get_menu_choice():
    print()
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")
    choice = input("Please enter the letter which corresponds with your desired menu choice: ") .upper()
    return choice

def get_export_choice():
    print()
    print("[T] Export as TXT")
    print("[C] Export as CSV")
    print("[J] Export as JSON")
    print("[X] Exit")
    choice = input("Please enter the letter which corresponds with your desired menu choice: ")
    return choice

def get_data_choice():
    print()
    print("[A] Most Reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Average Rating by Park and Year")
    print("[D] Average Rating by Park and Country")
    print("[X] Return to Main Menu")
    choice = input("Please enter the letter which corresponds with your desired menu choice: ") .upper()
    return choice

def get_park_name():
    print()
    print("[1] Disneyland_California")
    print("[2] Disneyland_Paris")
    print("[3] Disneyland_Hongkong")
    print("[X] Return to Main Menu")
    choice = input("Please enter the park number: ")
    return choice

def get_country_name():
    choice = input("Please enter a country name: ")
    return choice

def get_year():
    print()
    choice = input("Please enter a year: ")
    return choice

def get_visualise_choice():
    print()
    print("[A] Pie Chart - Reviews by Park")
    print("[B] Bar Chart - Top 10 Locations by Rating")
    print("[C] Bar Chart - Average Rating by Month")
    print("[X] Return to Main Menu")
    choice = input("Please enter the letter which corresponds with your desired menu choice: ")
    return choice
