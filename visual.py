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

