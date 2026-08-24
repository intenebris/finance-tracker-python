from models import (
    add_transaction,
    get_all_transactions,
    get_transaction_by_category,
    get_transaction_by_date,
    get_transaction_by_type
)

def print_transactions(rows):
    """Красивый вывод транзакций."""
    if not rows:
        print("\nНет данных.\n")
        return

    print("\n--- ТРАНЗАКЦИИ ---")
    for row in rows:
        id_, amount, category, type_, date, comment = row
        print(f"[{id_}] {date} | {type_.upper()} | {amount} руб | {category} | {comment or ''}")
    print("-------------------\n")

def add_transaction_menu():
    """Меню добавления транзакции."""
    print("\nДобавление транзакции:")
    amount = float(input("Сумма: "))
    category = input("Категория: ")
    type_ = input("Тип (income/expense): ").strip().lower()
    comment = input("Комментарий (необязательно): ")

    add_transaction(amount, category, type_, comment=comment)
    print("\nТранзакция добавлена!\n")
