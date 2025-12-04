📚 Library Inventory Manager – Anshuman Sharma

A simple, clean, and fully functional Python CLI project for managing a library’s inventory.
This project was created as part of the Python Semester-1 assignment.

🚀 Features

➕ Add new books

🔍 Search books by title or ISBN

📖 View all books

📤 Issue books

📥 Return books

💾 Data stored in JSON (persistent storage)

🧪 Includes unit test for main functionality

🗂 Project Structure
library-inventory-manager-anshuman/
│
├── cli/
│   └── main.py                 # CLI entry point
│
├── library_manager/
│   ├── book.py                 # Book model
│   └── inventory.py            # Inventory management logic
│
├── data/
│   └── catalog.json            # JSON database (auto-created)
│
├── tests/
│   └── test_inventory.py       # Unit test
│
├── .venv/                      # Virtual environment
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Setup Instructions (Mac / Windows / Linux)
1️⃣ Create & Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
# OR
.venv\Scripts\activate         # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application

Use this command to start the CLI menu:

python3 -m cli.main

🧪 Run Tests

To verify everything works correctly:

python3 -m unittest discover -v


Or run a specific test:

python3 -m unittest tests.test_inventory.InventoryTest -v

📝 Example Workflow
1 → Add Book  
4 → View All  
2 → Issue Book  
3 → Return Book  
7 → Exit  

🎯 Purpose of This Project

This project demonstrates:

Understanding of Python modules & packages

JSON file handling

Object-oriented programming (classes, methods)

CLI-based user interaction

Clean folder structure & unit testing

Perfect for academic submission and resume projects.

👨‍💻 Author

Anshuman Sharma
Python Semester-1 Project
KR Mangalam University
