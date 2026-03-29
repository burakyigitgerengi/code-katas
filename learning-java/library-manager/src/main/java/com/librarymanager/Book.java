package com.librarymanager;

public class Book {

    private int bookId;
    private String title;
    private String author;
    private boolean isAvailable;

    public Book(int bookId, String title, String author, boolean isAvailable) {

        this.bookId = bookId;
        this.title = title;
        this.author = author;
        this.isAvailable = isAvailable;

    }

    // GETTERS

    public int getBookId() {
        return this.bookId;
    }

    public String getTitle() {
        return this.title;
    }

    public String getAuthor() {
        return this.author;
    }

    public boolean getIsAvailable() {
        return this.isAvailable;
    }

    // SETTERS

    public void setBookId(int id) {
        this.bookId = id;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setIsAvailable(boolean bool) {
        this.isAvailable = bool;
    }

    // METHODS

    public void displayInfo() {

        String availability;

        if (getIsAvailable()) {
            availability = "Available";
        } else {
            availability = "Unavailable";
        }

        System.out.println("Book ID: " + getBookId());
        System.out.println("Book Title: " + getTitle());
        System.out.println("Book Author: " + getAuthor());
        System.out.println("Book Availablitiy: " + availability);

    }

}