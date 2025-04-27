from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
db = SQLAlchemy(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    print("Index route accessed!")  # Debugging statement
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    
    new_book = Book(title=title, author=author)
    db.session.add(new_book)
    db.session.commit()
    
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    
    return redirect("/")

# ⬇️ Move this to the very bottom:
if __name__ == "__main__":
    app.run(debug=True)
