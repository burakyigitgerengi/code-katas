package com.librarymanager;

public class User {

    private int userId;
    private String userName;
    private int borrowLimit = 5;

    public User(int userId, String userName) {
        this.userId = userId;
        this.userName = userName;
    }

    // GETTERS

    public int getUserId() {
        return this.userId;
    }

    public String getUserName() {
        return this.userName;
    }

    public int getBorrowLimit() {
        return this.borrowLimit;
    }

    // SETTERS

    public void setUserId(int id) {
        this.userId = id;
    }

    public void setUserName(String name) {
        this.userName = name;
    }

    public void setBorrowLimit(int limit) {
        this.borrowLimit = limit;
    }

    // METHODS

    public void displayInfo() {

        System.out.println("User ID: " + getUserId());
        System.out.println("User Name: " + getUserName());
        System.out.println("User Borrow Limit: " + getBorrowLimit() + "\n");

    }

}
