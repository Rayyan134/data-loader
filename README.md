# DataLoader Project

A simple Python project that demonstrates how to build a reusable **DataLoader class** for reading CSV files and working with structured data using object-oriented programming.

---

## 📁 Project Structure

```
data_loader/
│
├── data/
│   └── students.csv
│
├── src/
│   └── data_loader.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
```

## Features

- Load CSV files into Python objects
- Store data as a list of dictionaries
- Access records by index
- Count total records
- Print dataset summary
- Clean OOP-based design

---

## Example Dataset

**students.csv**
name,grade
Ali,85
Sara,92
John,70


---

## How It Works

The `DataLoader` class:

- Reads a CSV file
- Converts each row into a dictionary
- Stores all rows in `self.data`

Example internal structure:

```python
[
    {"name": "Ali", "grade": "85"},
    {"name": "Sara", "grade": "92"},
    {"name": "John", "grade": "70"}
]

