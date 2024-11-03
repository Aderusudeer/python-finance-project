from database import get_db_connection

def add_transaction(user_id, transaction_type, category, amount, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (user_id, type, category, amount, date) VALUES (?, ?, ?, ?, ?)",
                   (user_id, transaction_type, category, amount, date))
    conn.commit()
    conn.close()

def set_budget(user_id, category, monthly_budget):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO budgets (user_id, category, monthly_budget) VALUES (?, ?, ?)",
                   (user_id, category, monthly_budget))
    conn.commit()
    conn.close()
