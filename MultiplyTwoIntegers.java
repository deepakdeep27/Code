import java.util.Scanner;

public class MultiplyTwoIntegers {
    public static int multiplyTwoIntegers(int first, int second) {
        return first * second;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first integer: ");
        int firstNumber = scanner.nextInt();

        System.out.print("Enter second integer: ");
        int secondNumber = scanner.nextInt();

        System.out.println("Product = " + multiplyTwoIntegers(firstNumber, secondNumber));

        scanner.close();
    }
}
