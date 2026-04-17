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

def get_reviews_by_park(dataset):
    park_counts = {}
    for row in dataset[1:]:
        if row[4] not in park_counts:
            park_counts[row[4]] = 1
        else:
            park_counts[row[4]] += 1

    return park_counts



