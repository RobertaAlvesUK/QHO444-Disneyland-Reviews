"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

def process_data():
    with open("data/Disneyland_reviews.csv") as csv_file:
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
    sorted_park_counts = sorted (park_counts.items(), key = lambda x : x[1], reverse = True)

    return sorted_park_counts

def get_park_reviews(dataset, park_name):
    reviews = []
    for row in dataset[1:]:
        if row[4] == park_name:
            reviews.append(row)
    return reviews

def get_ratings_by_country(dataset):
    country_counts = {}
    for row in dataset[1:]:
        if row[3] not in country_counts:
            country_counts[row[3]] = 1
        else:
            country_counts[row[3]] += 1
    sorted_country_counts = sorted (country_counts.items(), key = lambda x : x[1], reverse = True)

    return sorted_country_counts


def get_park_months(dataset):
    park_months = {}
    for row in dataset[1:]:
        if row[4] not in park_months:
            park_months[row[4]] = {}
        if "-" in row[2]:
            month = row[2].split("-")[1]
            if month not in park_months[row[4]]:
                park_months[row[4]][month] = 1
            else:
                park_months[row[4]][month] += 1
    return park_months

def get_reviews_by_park_and_country(dataset, park_name, country_name):
    reviews = []
    for row in dataset:
        if row[4] == park_name and row[3] == country_name:
            reviews.append(row)
    return reviews

def get_avg_ratings_by_park_and_year(dataset, park_name, year):
    total = 0
    count = 0
    for row in dataset:
        if row[4] == park_name and row[2].startswith(year):
            total += int(row[1])
            count += 1
    if count > 0:
        return round(total/count, 2)
    else:
        return 0

def get_avg_ratings_by_country_for_park(dataset, park_name):
    total = {}
    count ={}
    for row in dataset[1:]:
        if row[4] == park_name:
            country = row[3]
            if country not in total:
                total[country] = 0
                count[country] = 0
            total[country] += int(row[1])
            count[country] += 1
    average = {}
    for country in total:
       average[country] = round(total[country]/count[country], 2)
    sorted_average = sorted(average.items(), key=lambda x: x[1], reverse=True)
    return sorted_average[:10]

