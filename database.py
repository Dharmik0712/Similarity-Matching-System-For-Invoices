import sqlite3

def init_db():
    conn = sqlite3.connect('invoices.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY,
            file_name TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_invoice(file_name, content):
    conn = sqlite3.connect('invoices.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO invoices (file_name, content) VALUES (?, ?)', (file_name, content))
    conn.commit()
    conn.close()

def get_all_invoices():
    conn = sqlite3.connect('invoices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT file_name, content FROM invoices')
    invoices = cursor.fetchall()
    conn.close()
    return invoices
