"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt
def pie_chart_reviews_by_park(park_counts):
    labels = [item[0] for item in park_counts]
    values = [item[1] for item in park_counts]
    plt.pie(values, labels=labels)
    plt.title("Reviews by Park")
    plt.show()

def bar_chart_avg_by_country(top_countries):
    x = [item[0] for item in top_countries]
    y = [item[1] for item in top_countries]
    plt.bar(x, y)
    plt.xticks(rotation=45, ha="right")
    plt.title("Average Reviews by Country")
    plt.tight_layout()
    plt.show()

def bar_chart_avg_by_month(monthly_data):
    x = [item[0] for item in monthly_data]
    y = [item[1] for item in monthly_data]
    plt.bar(x, y)
    plt.title("Average Reviews by Month")
    plt.show()