import streamlit as st
import pandas as pd
from library_db import LibraryDatabase

# Initialize the database
db = LibraryDatabase()

# Set up Streamlit UI
st.title("📚 Library Management System")

# Input for adding books
title = st.text_input("Book Title")
author = st.text_input("Author Name")

if st.button("➕ Add Book"):
    db.add_book(title, author)
    st.success(f"Added '{title}' by {author}")

# Fetch stored books
books = db.get_books()

if books:
    # Convert books to a DataFrame for easy display
    df = pd.DataFrame(books, columns=["ID", "Title", "Author"])
    
    # Show books as a table
    st.subheader("📖 Available Books")
    st.dataframe(df)

    # Add book deletion option
    book_id = st.number_input("Enter Book ID to Delete", min_value=1)
    if st.button("❌ Delete Book"):
        db.delete_book(book_id)
        st.warning(f"Deleted book with ID {book_id}")
else:
    st.info("No books in the library yet. Add a new book above!")
