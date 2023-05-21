using System;


class Program{

  static public void mergeSort(int[] array, int start, int end){
	if(end <= start) return;
 	int midpoint = (end + start) / 2 ;	
  	mergeSort(array, start, midpoint);
	mergeSort(array, midpoint + 1, end);
  	merge(array, start, midpoint, end);

  }
	
  static public void merge(int[] array, int start, int midpoint, int end){
  	int i, j, k;
	int left_length = midpoint - start  + 1 ;
	int right_length = end - midpoint ;
	int[] left_array = new int[left_length];
	int[] right_array = new int[right_length];

	for(i = 0; i < left_length; i++){
	  left_array[i] = array[start + i];
	}

	for(j = 0; j < right_length; j++){
	  right_array[j] = array[midpoint + 1 + j];
	}


	i = j = 0;
	k = start;
	while(i < left_length && j < right_length){
		if(left_array[i] <= right_array[j]){
		  array[k] = left_array[i];
		  i++;
		}else{
	          array[k] = right_array[j];
		  j++;
		}
		k++;
	}

	while(i < left_length){
	  array[k] = left_array[i];
	  i++;
	  k++;
	}
	
	while(j < right_length){
	  array[k] = right_array[j];
	  j++;
	  k++;
	}
  } 
  
  public static void Main (string[] args){
  	
  	int[] array = {9, 5, 1, 4};
	Console.WriteLine( String.Join(", ", array) );
	mergeSort(array, 0, array.Length - 1 );
	Console.WriteLine( String.Join(", ", array) );
  }


}
