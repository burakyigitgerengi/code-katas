import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (true) {

            System.out.println("=== Calculator ===\r\n" + //
                    "Enter two numbers.");

            System.out.println("Please enter the first number: ");
            String num1Str = sc.nextLine();

            System.out.println("Please enter the second number: ");
            String num2Str = sc.nextLine();

            double num1 = Double.parseDouble(num1Str);
            double num2 = Double.parseDouble(num2Str);

            System.out.println("=== Calculator ===\r\n" + //
                    "1 Add\r\n" + //
                    "2 Subtract\r\n" + //
                    "3 Multiply\r\n" + //
                    "4 Divide\r\n" + //
                    "0 Exit\r\n" + //
                    "Enter your desire: ");

            String selection = sc.nextLine();

            double result = 0;

            switch (selection) {
                case "0":
                    System.out.println("Goodbye!");
                    sc.close();
                    return;

                case "1":
                    System.out.println("Let's add some numbers!");

                    result = num1 + num2;
                    System.out.println(result);

                    break;

                case "2":
                    System.out.println("Let's substract some numbers!");

                    result = num1 - num2;
                    System.out.println(result);

                    break;

                case "3":
                    System.out.println("Let's multiply some numbers!");

                    result = num1 * num2;
                    System.out.println(result);

                    break;

                case "4":
                    System.out.println("Let's divide some numbers!");

                    if (num2 == 0) {
                        System.out.println("Oops! Can't divide a number by zero.");
                        break;
                    }

                    else {
                        result = num1 / num2;
                        System.out.println(result);
                    }

                    break;

                default:
                    System.out.println("No options found... Maybe wrong key pressed?");
            }

        }

        // sc.close();

    }

}
