from math import sqrt


def mean(array: list) -> float:
    mean = 0
    for number in array:
        mean += number
    return mean / len(array)


def standard_deviation(array: list) -> float:
    summation = 0
    the_mean = mean(array)
    for index, element in enumerate(array):
        summation += (element - the_mean)**2 

    summation = summation / len(array)
    return sqrt(summation)


print(standard_deviation([10, 12, 23, 23, 16, 23, 21, 16]))
print(standard_deviation([10, 12, 23, 21, 16]))

