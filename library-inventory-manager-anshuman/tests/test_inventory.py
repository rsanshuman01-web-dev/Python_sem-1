import unittest
from pathlib import Path
import tempfile
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.tmpfile = Path(tempfile.mktemp(suffix=".json"))
        self.inv = LibraryInventory(self.tmpfile)

    def tearDown(self):
        try:
            self.tmpfile.unlink()
        except Exception:
            pass

    def test_add_search_issue_return(self):
        b = Book("Test Book", "Author Name", "ISBN123")
        self.inv.add_book(b)
        found = self.inv.search_by_isbn("ISBN123")
        self.assertIsNotNone(found)
        self.inv.issue_book("ISBN123")
        self.assertFalse(found.is_available())
        self.inv.return_book("ISBN123")
        self.assertTrue(found.is_available())

if __name__ == "__main__":
    unittest.main()
