def binarySearch(array: list, key: int):
    start: int = 0
    end: int = len(array)-1
    middle: int = (start + end) // 2
    while(start <= end):
        if array[middle] == key:
            return middle
        elif array[middle] > key:
            end = middle - 1
            middle = (start + end) // 2 
                        
        else:    
            start = middle + 1
            middle = (start + end) // 2 
            
        return "Not found"
    return middle


array: list = [1, 2, 3, 4, 5, 6]
print("Array: ", array)
print("Value 1 at index: ", binarySearch(array, 1))
print("Value 5 at index: ", binarySearch(array, 5))
print("Value 6 at index: ", binarySearch(array, 6))
print("Value 99 is ", binarySearch(array, 99))
