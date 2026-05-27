import java.util.Scanner;

public class Timer {

    public static int getUserTime() {

        System.out.println("Welcome to my timer script!");

        Scanner input = new Scanner(System.in);
        System.out.println("Please input the time you wish to set:");
        int timeInputFromUser = input.nextInt();
        input.close();

        return timeInputFromUser;

    }

    public static void timer(int time) {

        System.out.println("Timer started!");

        for (int i = time; i != -1; --i) {

            System.out.println(i);

            if (i == 0) {

                System.out.println("Time you've set is over!");
                break;
            }

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println("Timer interrupted");
            }

        }

    }

    public static void main(String[] args) {

        int userTime = getUserTime();
        timer(userTime);

    }

}
