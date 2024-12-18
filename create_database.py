import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('bank_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table for bank branches
cursor.execute('''
CREATE TABLE IF NOT EXISTS branches (
    ifsc TEXT PRIMARY KEY,
    branch TEXT,
    bank_name TEXT
)
''')

# Save changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
