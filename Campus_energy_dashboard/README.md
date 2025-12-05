# Campus Energy Dashboard – Anshuman Sharma

**Course:** Programming for Problem Solving using Python  
**Assignment:** Capstone Project – End-to-End Energy Consumption Analysis  
**Student Name:** Anshuman Sharma  
**Date:** 5 December 2024  

---

## 📌 Project Objective
This project analyzes electricity consumption of campus buildings.  
It loads meter data from CSV files, processes and summarizes it, and generates:

- A cleaned combined dataset  
- Daily & weekly aggregates  
- Building-wise consumption summary  
- A 3-chart dashboard (PNG)  
- A textual summary report  

---

## 📂 Folder Structure

Campus_energy_dashboard/
│
├── data/ # Input CSV files
├── src/ # Python scripts (pipeline)
├── output/ # Generated files
└── submission/ # Final files for teacher

yaml
Copy code

---

## ▶️ How to Run the Project

1. Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

markdown
Copy code

2. Install required packages:
pip install pandas matplotlib python-dateutil pytz

markdown
Copy code

3. Run the script:
python src/main.py

yaml
Copy code

All output files will appear in the `output/` folder.  
Final submission files are in the `submission/` folder.

---

## 📑 Final Submission Files

Inside the **submission** folder:

- `dashboard.png`  
- `cleaned_energy_data.csv`  
- `building_summary.csv`  
- `summary.txt`  

These 4 files are required for grading.

---

## 📊 Dashboard Preview
The dashboard contains:
- Daily energy trend (line chart)  
- Weekly average usage (bar chart)  
- Peak daily load per building (scatter plot)  

---

## ✔ Result Summary (auto-generated)
See `submission/summary.txt` for:
- Total campus consumption  
- Highest consuming building  
- Peak load timestamp  

---

## ✅ Academic Integrity
This is an individual assignment.  
All code is written from scratch following the assignment guidelines.

