package com.librarymanager;

import java.util.HashMap;
import com.google.gson.Gson;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Library {

    private HashMap<Integer, Book> books;
    private HashMap<Integer, User> users;

    public Library() {

        books = new HashMap<>();
        users = new HashMap<>();
        loadFromJson();

    }

    // VARIABLES

    private String databaseFile = "data/database.json";
    Gson gson = new Gson();

    // JSON METHODS

    public void loadFromJson() {
        try (FileReader reader = new FileReader(databaseFile)) {
            Library loadedLibrary = gson.fromJson(reader, Library.class);
            if (loadedLibrary != null) {
                this.books = loadedLibrary.books;
                this.users = loadedLibrary.users;
            }
        } catch (IOException e) {
            System.out.println("Error loading database: " + e.getMessage());
            // Initialize empty if file not found
        }
    }

    public void saveToJson() {
        try (FileWriter writer = new FileWriter(databaseFile)) {
            gson.toJson(this, writer);
        } catch (IOException e) {
            System.out.println("Error saving database: " + e.getMessage());
        }
    }

    // METHODS

    public void showAllBooks() {

        if (books.size() == 0) {
            System.out.println("This library doesn't have any books.");
        }

        int index = 1;
        for (Book book : books.values()) {
            System.out.println(index);
            book.displayInfo();
            index++;
        }

    }

    public void borrowBook(int userId, int bookId) {

        if (!users.containsKey(userId)) {
            System.out.println("Borrow failed: User not found.");
            return;
        }

        else if (!books.containsKey(bookId)) {
            System.out.println("Borrow failed: Book not found.");
            return;
        }

        Book bookToBorrow = books.get(bookId);
        if (!bookToBorrow.getIsAvailable()) {
            System.out.println("Borrow failed: Book not available.");
            return;
        }

        User borrower = users.get(userId);
    }

}
