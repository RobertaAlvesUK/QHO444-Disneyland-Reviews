
"""
This module contains information about Disney Reviews Dataset to export
data when is necessary.
"""
import csv
import json

class ExportDisney:
    def __init__(self, dataset):
        self.dataset = dataset
    def get_park_stats(self):
        reviews_count = {}
        positive_reviews = {}
        rating_total = {}
        countries = {}

        for review in self.dataset[1:]:
            park = review[4]

            if park not in reviews_count:
                reviews_count[park] = 0
            reviews_count[park] += 1

            if park not in positive_reviews:
                positive_reviews[park] = 0
            if int(review[1]) >= 4:
                positive_reviews[park] += 1

            if park not in rating_total:
                rating_total[park] = 0
            rating_total[park] += int(review[1])

            if park not in countries:
                countries[park] = set()
            countries[park].add(review[3])

        stats = {}
        for park in reviews_count:
            avg_rating = round(rating_total[park] / reviews_count[park], 2)
            stats[park] = {
                "reviews": reviews_count[park],
                "positive": positive_reviews[park],
                "avg_rating": avg_rating,
                "countries": len(countries[park]),
            }
        return stats

    def export_txt(self, stats):
        with open("disney_export.txt", "w") as file:
            for park in stats:
                file.write(f"Park: {park}\n")
                file.write(f"Reviews: {stats[park]['reviews']}\n")
                file.write(f"Positive reviews: {stats[park]['positive']}\n")
                file.write(f"Average rating: {round(stats[park]['avg_rating'], 2)}\n")
                file.write(f"Countries: {stats[park]['countries']}\n")
                file.write("___\n")

    def export_csv(self, stats):
        with open("disney_export.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Park", "Reviews", "Positive Reviews", "Average Rating", "Countries"])
            for park in stats:
                writer.writerow([park, stats[park]['reviews'], stats[park]['positive'], stats[park]['avg_rating'], stats[park]['countries'] ])

    def export_json(self, stats):
        with open("disney_export.json", "w", encoding="utf-8") as file:
            json.dump(stats, file, indent=4)








        


