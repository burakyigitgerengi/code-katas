package librarymanager.src;

public class LibraryManager {
    public static void main(String[] args) {

        User user1 = new User(31, "Aziz");

        System.out.println(user1.getBorrowLimit());

    }

}