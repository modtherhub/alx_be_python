from library_system import Book, EBook, PrintBook, Library

def main():
    lib = Library()
    lib.add_book(PrintBook("The Hobbit", "J.R.R. Tolkien", 1937, 310))
    lib.add_book(EBook("Digital Fortress", "Dan Brown", 1998, "2MB"))

    lib.list_books()

if __name__ == "__main__":
    main()
