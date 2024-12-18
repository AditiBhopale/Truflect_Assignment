import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('bank_data.db')
cursor = conn.cursor()

# Open the CSV file containing the data
with open('bank_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    # Insert each row into the branches table
    for row in csv_reader:
        cursor.execute('INSERT OR IGNORE INTO branches (ifsc, branch, bank_name) VALUES (?, ?, ?)', row)

# Save changes and close the connection
conn.commit()
conn.close()

print("Data has been populated successfully.")
