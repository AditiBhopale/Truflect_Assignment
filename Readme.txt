# Advertisement Assignment API

This project is a Python-based web API built using Flask. It provides endpoints to fetch details about banks and their branches from an SQLite database.

---

## Features

- List all banks in the database.
- Fetch branch details for a specific bank.
- Handles errors gracefully (e.g., invalid bank names return a 404 error).

---

## Technology Stack

- **Programming Language:** Python 3.12.2
- **Framework:** Flask
- **Database:** SQLite
- **Tools for Testing:** pytest

---

## Setup Instructions

### 1. Clone the Repository
Clone this project into your local machine:
```bash
git clone <your-repo-url>
cd <project-folder>

### 2. Setup a virtual Environment
python -m venv venv(Activate the virtual Environment)
venv\Scripts\activate

### 3. pip install -r requirements.txt
### 4. python populate_database.py
### 5. python app.py
 This will run on the port http://127.0.0.1:5000

### 6. To get banks
visit  http://127.0.0.1:5000/banks

Sample response
[
    "Example Bank",
    "Sample Bank"
]
### TO get branches/bank_name
visit http://127.0.0.1:5000/branches/Example%20Bank

Response

[
    {"ifsc": "ABCD0123456", "branch": "Main Branch"},
    {"ifsc": "WXYZ0987654", "branch": "Secondary Branch"}
]

### To test the API
pytest test_api.py

Expected Output

============================= test session starts =============================
platform win32 -- Python 3.12.2, pytest-8.3.4, pluggy-1.5.0
rootdir: <project-folder>
collected 3 items

test_api.py ...                                                               [100%]

============================= 3 passed in 0.50s ==============================


Time taken to complete this assignment was approx 2 days

Author name: Aditi Bhopale
Email-id: aditibhopale0618@gmail.com