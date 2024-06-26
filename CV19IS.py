# Third Case Study : COVID 19 Infection Statistic
# • (COVID-19 Infection Statistics) During the first 20 days of the COVID-19 pandemic, the number
#   of newly infected patients per day in a country were recorded.
# • Place the following numbers in a list: 174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301,
#   1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342 Use the built-in functions in the statistics
#   module to display the following statistics concerning the infection rate: minimum, maximum,
#   range, mean, median, variance, and standard deviation.

import statistics

# data list given from the problem
infection_data = [
    174, 335, 278, 214, 422, 513, 737, 672, 489, 412,
    1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342
]

minimum = min(infection_data)
maximum = max(infection_data)
range_value = maximum - minimum
mean = statistics.mean(infection_data)
median = statistics.median(infection_data)
variance = statistics.variance(infection_data)
standard_deviation = statistics.stdev(infection_data)

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {standard_deviation:.2f}")
