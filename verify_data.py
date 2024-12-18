import sqlite3

conn = sqlite3.connect('bank_data.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM branches')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
