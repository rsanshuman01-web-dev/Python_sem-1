GradeBook Analyzer CLI

A Python-based command-line tool that reads student marks (manual input or CSV), computes key statistics, assigns grades, and produces a formatted results table. This project automates common lecturer tasks like calculating averages, distributing grades, and filtering pass/fail students.

⸻

📌 Features
	•	Manual student entry or CSV file import
	•	Statistical calculations:
	•	Mean (average)
	•	Median
	•	Maximum & minimum scores
	•	Automatic grade assignment (A–F scale)
	•	Grade distribution summary
	•	Pass/Fail classification using list comprehension
	•	Clean and formatted results table
	•	Optional export of final results to CSV
	•	Menu-driven CLI loop for repeated use

⸻

📁 Project Structure

gradebook_analyzer/
│── gradebook.py
│── students.csv   (sample input file)
│── final_grades.csv (generated after export)


⸻

▶️ How to Run the Program
	1.	Open a terminal in the project folder.
	2.	Run:

python gradebook.py


	3.	Choose from the menu:
	•	1 → Manual entry of students
	•	2 → Load students from CSV
	•	3 → Show currently loaded data
	•	4 → Run full analysis
	•	5 → Clear all data
	•	6 → Exit the program

⸻

📄 CSV Input Format (students.csv)

Your CSV must contain the following columns:

Name,Marks
Alice,78
Bob,92
Charlie,65
Deepa,55
Eve,38


⸻

📊 Analysis Output Includes
	•	Total number of students
	•	Average score
	•	Median score
	•	Highest & lowest score with student names
	•	Grade distribution (A–F)
	•	List of passed and failed students
	•	Tabular display:

Name            Marks     Grade
-----------------------------------
Alice           78        C
Bob             92        A
...


⸻

💾 Exporting Results

After analysis, the program will ask:

Export results table to CSV? (y/N):

Type y, then provide a filename (e.g., final_grades.csv). The exported file will contain:

Name,Marks,Grade
Alice,78,C
Bob,92,A
...


⸻

📚 Learning Objectives 
	•	Reading input manually or from CSV
	•	Working with Python dictionaries & lists
	•	Implementing custom statistical functions
	•	Using control flow for grade assignment
	•	Using list comprehensions for pass/fail filtering
	•	Practice modular programming with functions
	•	Formatting CLI output with f-strings and loops

⸻

🧑‍💻 Author

Your: Anshuman Sharma
Date: 22-11-2025
