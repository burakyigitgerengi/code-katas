package librarymanager.src;

import java.util.ArrayList;

public class User {

    private int id;
    private String name;
    private int borrowLimit = 5;
    private ArrayList<Integer> borrowedBooks = new ArrayList<Integer>();

    public User(int id, String name) {
        this.id = id;
        this.name = name;
    }

    // GETTERS

    public int getUserId() {
        return this.id;
    }

    public String getUserName() {
        return this.name;
    }

    public int getBorrowLimit() {
        return this.borrowLimit;
    }

    public ArrayList<Integer> getBorrowedBooks() {
        return this.borrowedBooks;
    }

    // SETTERS

    public void setBorrowLimit(int limit) {

        this.borrowLimit = limit;

    }

    // METHODS

}
