def insertionSort(array: list):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while(j >= 0 and key < array[j]):
            if array[j] > key:
                array[j+1] = array[j]
            j = j - 1
        array[j+1] = key

    return array


print(insertionSort([1, 3, 5, 0, 4]))   
    
