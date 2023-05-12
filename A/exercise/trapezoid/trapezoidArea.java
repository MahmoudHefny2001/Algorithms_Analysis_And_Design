package A.exercise.trapezoid;

public class trapezoidArea{
    public static void main(String[] args) {
        System.out.println(trapezoid_area(5, 6, 7));
        System.out.println(trapezoid_area(3, 4, 5));
    }

    private static double trapezoid_area(float a, float b, float h) {
        double area = ( ( ( a + b ) / 2 )  * h );
        return area;
    } 
}