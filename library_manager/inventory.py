import json
from pathlib import Path
from typing import List, Optional
from .book import Book
import logging

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, json_path: Path):
        self.json_path = Path(json_path)
        self.books: List[Book] = []
        self.load()

    def load(self):
        try:
            if not self.json_path.exists():
                logger.info("Catalog file not found. Creating new one.")
                self.save()
                return
            with self.json_path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            self.books = [Book(**item) for item in data]
            logger.info("Loaded %d books from catalog.", len(self.books))
        except json.JSONDecodeError:
            logger.error("Catalog file is corrupted. Starting with empty catalog.")
            self.books = []
        except Exception as e:
            logger.exception("Unexpected error while loading catalog: %s", e)
            self.books = []

    def save(self):
        try:
            self.json_path.parent.mkdir(parents=True, exist_ok=True)
            with self.json_path.open('w', encoding='utf-8') as f:
                json.dump([b.to_dict() for b in self.books], f, indent=2)
            logger.info("Saved %d books to catalog.", len(self.books))
        except Exception:
            logger.exception("Failed to save catalog.")

    def add_book(self, book: Book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("A book with this ISBN already exists.")
        self.books.append(book)
        self.save()

    def search_by_title(self, title: str) -> List[Book]:
        q = title.lower()
        return [b for b in self.books if q in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[Book]:
        return list(self.books)

    def issue_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found.")
        book.issue()
        self.save()

    def return_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found.")
        book.return_book()
        self.save()
