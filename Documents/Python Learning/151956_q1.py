class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is already borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
        else:
            print (f"{self.name} did not borrow '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")


def main():
    # Create sample books
    book1 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
    book2 = Book("Goosebumps", "R.Stirley")
    book3 = Book("The Lincoln Lawyer", "John Grisham")

    # Creating a library member
    member = LibraryMember("Alice", 1)

    
    member.borrow_book(book1)   # Alice borrows Diary of a Wimpy Kid
    member.borrow_book(book2)   # Alice borrows Goosebumps
    member.borrow_book(book1)   # Attempt to borrow Diary of a Wimpy Kid again
    member.list_borrowed_books() # List Alice's borrowed books

    member.return_book(book1)   # Alice returns Diary of a Wimpy kid
    member.return_book(book3)   # Attempt to return a book not borrowed
    member.list_borrowed_books() # List Alice's borrowed books

main()
