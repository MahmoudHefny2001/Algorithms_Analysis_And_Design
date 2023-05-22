function greedySelection(startTime, endTime){
    results = [0];
    j = 0;

    for (var i = 1; i < startTime.length; i++){
        if(startTime[i] >= endTime[j]){
            results.push(i);
            j = i;
        }
    }
    
    console.log(results);
}


start = [9, 10, 11, 12, 13, 15];
end = [11, 11, 12, 14, 15, 16];

greedySelection(start, end);
