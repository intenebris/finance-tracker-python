from ui_console import main_menu
from database import create_tables

def main():
    # Создаём таблицы, если их нет
    create_tables()

    # Запускаем консольное меню
    main_menu()

if __name__ == '__main__':
    main()