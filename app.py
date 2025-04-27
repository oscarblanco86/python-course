import sqlite3
import streamlit as st

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
                author TEXT
            )
        """)
        self.conn.commit()

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.conn.commit()

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()



# Initialize the database
library_db = LibraryDatabase()

st.title("📚 Library Management App")

# Add a book
title = st.text_input("Book Title")
author = st.text_input("Author Name")

if st.button("Add Book"):
    library_db.add_book(title, author)
    st.success(f"Added '{title}' by {author}")

# Show all books
st.subheader("📖 Available Books")
books = library_db.get_books()
for book in books:
    st.write(f"📘 {book[1]} by {book[2]}")
