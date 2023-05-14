from math import sqrt

def summationOfArrayElements(array: list) -> int:
    summation = 0
    if array is not None:
        for element in array:
            summation += element
    
    return summation
    

def mean(array: list) -> float:
    return summationOfArrayElements(array) / len(array)


def twoListMultiplication(array1: list, array2: list) -> list:
    new_list = []
    i = 0
    while(i < len(array1)):
        new_list.append(array1[i] * array2[i])
        i += 1
    return new_list


def correlation(array1: list, array2: list) -> float:
    x_mean = mean(array1)
    y_mean = mean(array2)
    
    a = []
    b = []

    for x_elemnt in array1:
        a.append(x_mean - x_elemnt)

    for y_elemnt in array2:
        b.append(y_mean - y_elemnt)

    
    ab = twoListMultiplication(a, b)
    a_square = twoListMultiplication(a, a)
    b_square = twoListMultiplication(b, b)

    ab_sum = summationOfArrayElements(ab)
    a_sum = summationOfArrayElements(a_square)
    b_sum = summationOfArrayElements(b_square)

    return summationOfArrayElements(ab) / sqrt(a_sum * b_sum)

print(correlation((10, 5, 50, 60), (20, 30, 70, 10)))

