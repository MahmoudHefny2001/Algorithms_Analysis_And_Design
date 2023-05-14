package InsertionSort;

public class InsertionSort{
    public static void main(String[] args) {
        double[] array = {9, 5, 1, 4, 3};
        double[] sortedArray = insertion_Sort(array);
        for (double element : sortedArray) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    private static double[] insertion_Sort(double[] array){
        int i, j = 0;
        for(i = 1; i < array.length; i++){
            double key = array[i];
            for(j = i - 1; j >= 0; --j){
                if(array[j] > key){
                    array[j+1] = array[j]; 
                }
                else{
                    break;
                }
            }
            array[j+1] = key;
        }
        return array;
    }
    
}
