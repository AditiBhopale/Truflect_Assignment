from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('bank_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get a list of all banks
@app.route('/banks', methods=['GET'])
def get_banks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT bank_name FROM branches')
    banks = [row['bank_name'] for row in cursor.fetchall()]
    conn.close()
    return jsonify(banks)

# Get branch details for a specific bank
@app.route('/branches/<bank_name>', methods=['GET'])
def get_branches(bank_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ifsc, branch FROM branches WHERE bank_name = ?', (bank_name,))
    branches = [{'ifsc': row['ifsc'], 'branch': row['branch']} for row in cursor.fetchall()]
    conn.close()
    
    # Check if no branches are found for the given bank_name
    if not branches:
        return jsonify({"error": f"No branches found for bank: {bank_name}"}), 404
    
    return jsonify(branches)

