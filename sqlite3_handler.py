import sqlite3

class LibraryDatabase:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                is_available INTEGER
            )
        """)
        self.conn.commit()

    def add_book(self, book):
        self.cursor.execute("INSERT INTO books (title, author, is_available) VALUES (?, ?, ?)", 
                            (book.title, book.author, book.is_available))
        self.conn.commit()

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

# Example usage
library_db = LibraryDatabase()
library_db.add_book(Book("1984", "George Orwell"))
library_db.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# Retrieve books from database
books = library_db.get_books()
print("Library Books:", books)
