function insertionSort(array){
    for (let i = 1; i < array.length; i++) {
        let key = array[i];
        for (var j = i-1; j >= 0; j--) {
            if(array[j] > key){
                array[j+1] = array[j];

            }
            else{
                break;
            }
        }
        array[j+1] = key; 
    }
    console.log(array);
}



insertionSort([9, 5, 1, 4, 3]);