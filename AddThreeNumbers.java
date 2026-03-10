import java.util.Scanner;

public class AddThreeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double first = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double second = scanner.nextDouble();

        System.out.print("Enter third number: ");
        double third = scanner.nextDouble();

        double sum = first + second + third;
        System.out.println("Sum = " + sum);

        scanner.close();
    }
}
