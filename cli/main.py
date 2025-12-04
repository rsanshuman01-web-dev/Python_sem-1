#!/usr/bin/env python3
import logging
from pathlib import Path
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "catalog.json"

def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty.")

def print_books(books):
    if not books:
        print("No books found.")
        return
    for b in books:
        print(f"- {b}")

def main():
    inv = LibraryInventory(DATA_FILE)
    menu = """
Library Inventory Manager
1. Add Book
2. Issue Book
3. Return Book
4. View All
5. Search by Title
6. Search by ISBN
7. Exit
Choose an option (1-7): """
    while True:
        try:
            choice = input(menu).strip()
            if choice == "1":
                title = input_nonempty("Title: ")
                author = input_nonempty("Author: ")
                isbn = input_nonempty("ISBN: ")
                try:
                    inv.add_book(Book(title=title, author=author, isbn=isbn))
                    print("Book added.")
                except ValueError as e:
                    print("Error:", e)

            elif choice == "2":
                isbn = input_nonempty("ISBN to issue: ")
                try:
                    inv.issue_book(isbn)
                    print("Book issued.")
                except Exception as e:
                    print("Error:", e)

            elif choice == "3":
                isbn = input_nonempty("ISBN to return: ")
                try:
                    inv.return_book(isbn)
                    print("Book returned.")
                except Exception as e:
                    print("Error:", e)

            elif choice == "4":
                print_books(inv.display_all())

            elif choice == "5":
                q = input_nonempty("Title search: ")
                print_books(inv.search_by_title(q))

            elif choice == "6":
                isbn = input_nonempty("ISBN search: ")
                book = inv.search_by_isbn(isbn)
                if book:
                    print(book)
                else:
                    print("Not found.")

            elif choice == "7":
                print("Exiting. Bye.")
                break

            else:
                print("Invalid option. Enter 1-7.")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break
        except Exception as e:
            logger.exception("Unexpected error: %s", e)
            print("An unexpected error occurred. Check logs.")

if __name__ == "__main__":
    main()
