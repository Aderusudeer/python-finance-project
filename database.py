import sqlite3

def get_db_connection():
    conn = sqlite3.connect("finance_manager.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT CHECK(type IN ('income', 'expense')),
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT NOT NULL,
            monthly_budget REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    ''')
    conn.commit()
    conn.close()
