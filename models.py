from database import get_connection
from datetime import datetime

def add_transaction(amount: float, category: str, type_: str, date: str = None, comment: str = None):
    """Добавление транзакции в базу данных."""
    if type_ not in("income", "expense"):
        raise ValueError("type_ должен быть 'income' или 'expense'")

    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (amount, category, type, date, comment)
        VALUES (?, ?, ?, ?, ?)
    """, (amount, category, type_, date, comment))

    conn.commit()
    conn.close()

def get_all_transactions():
    """Получить все транзакции."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows

def get_transaction_by_type(type_: str):
    """Получить только доходы или только расходы."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE type = ?
        ORDER BY date DESC
    """, (type_,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def get_transaction_by_category(category: str):
    """Получить транзакции по категории."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE category = ?
        ORDER BY date DESC
    """, (category,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def get_transaction_by_date(date: str):
    """Получить транзакции за конкретную дату (формат YYYY-MM-DD)."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE date = ?
        ORDER BY id DESC
    """, (date,))

    rows = cursor.fetchall()
    conn.close()
    return rows
