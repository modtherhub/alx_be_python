from library_system import Book, EBook, PrintBook, Library

def main():
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_book = EBook("Snow Crash", "Neal Stephenson", "500KB")
    printed_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    lib = Library()
    lib.add_book(classic_book)
    lib.add_book(digital_book)
    lib.add_book(printed_book)

    lib.list_books()

if __name__ == "__main__":
    main()
