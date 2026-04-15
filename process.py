"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

def process_data():
    csv_file = open("data/Disneyland_reviews.csv")
    csv_reader = csv.reader(csv_file)

    dataset = list(csv_reader)
    return dataset