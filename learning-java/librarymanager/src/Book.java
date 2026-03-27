package librarymanager.src;

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

    public boolean getIsAvailable() {

        return this.isAvailable;

    }

    public String getTitle() {

        return this.title;

    }

    public String getAuthor() {

        return this.author;
    }

    // SETTERS

    public void setIsAvailable(boolean bool) {
        this.isAvailable = bool;
    }

    // METHODS

    public void displayInfo() {

        String availability;

        if (this.isAvailable) {
            availability = "Available";
        } else {
            availability = "Unavailable";
        }

        System.out.println("ID:" + this.bookId);
        System.out.println("Title:" + this.title);
        System.out.println("Author:" + this.author);
        System.out.println("Availability" + availability);

    }

}