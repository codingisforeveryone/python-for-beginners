# Class Composition

Composition is when a `class` contains other objects as part of its data.

### 👨‍💻 TASK 1: Create a Book Class

Create a file called book.py:
```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"{self.title} by {self.author}")
```

### 👨‍💻 TASK 2: Create a Library Class (Composition)

Create a file called library.py:
```
from book import Book

class Library:
    def __init__(self):
        self.books = []   # Library contains a list of Book objects

    def add_book(self, title, author):
        new_book = Book(title, author)  # Create a Book object
        self.books.append(new_book)

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        
        for book in self.books:
            book.show_info()
```

### 👨‍💻 TASK 3: Test Composition

Create a file called test_library.py:
```
from library import Library

my_library = Library()

# Add some books
my_library.add_book("1984", "George Orwell")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
my_library.add_book("The Hobbit", "J.R.R. Tolkien")

my_library.show_books()
```

Run in terminal:
```
python test_library.py
```

## Summary

| Concept     | Explanation                                                           |
| ----------- | --------------------------------------------------------------------- |
| Composition | Library contains Book objects                                         |
| Attribute   | `self.books` is a list of Book objects inside Library                 |
| Method      | Library methods interact with Book objects |
| Advantage   | Reuse code and organize related objects logically                     |

