import json

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def save_to_json(self, filename="library.json"):
        with open(filename, "w") as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def load_from_json(self, filename="library.json"):
        with open(filename, "r") as f:
            book_data = json.load(f)
            self.books = [Book(**data) for data in book_data]

class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

# Example usage
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# Save to JSON
library.save_to_json()

# Load from JSON
library.load_from_json()
print("Library Books:", [book.title for book in library.books])
