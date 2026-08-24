import sqlite3
from pathlib import Path

DB_PATH = Path("data/finance.db")

def get_connection():
    """Подключение к базе данных."""
    DB_PATH.parent.mkdir(exist_ok=True) # Создаём папку data, если её нет
    return sqlite3.connect(DB_PATH)

def create_tables():
    """Создание таблиц, если их нет."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            date TEXT NOT NULL,
            comment TEXT
        );
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()