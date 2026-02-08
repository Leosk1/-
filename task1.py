from abc import ABC
from typing import Any


class Book(ABC):
    """
    Класс, представляющий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Инициализация экземпляра класса Book.

        Args:
            title: Название книги. Не может быть пустой строкой.
            author: Автор книги. Не может быть пустой строкой.
            year: Год издания. Должен быть положительным числом не больше текущего года.

        Raises:
            ValueError: Если название или автор пусты, или год некорректен.

        Examples:
            >>> book = Book("Война и мир", "Лев Толстой", 1869)
            >>> book.title
            'Война и мир'
        """
        if not title:
            raise ValueError("Название книги не может быть пустым")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год издания должен быть положительным целым числом")

        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        Returns:
            Строка с информацией о книге.

        Examples:
            >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
            >>> book.get_info()
            'Мастер и Маргарита, Михаил Булгаков, 1967'
        """
        return f"{self.title}, {self.author}, {self.year}"

    def is_classic(self, current_year: int) -> bool:
        """
        Проверяет, является ли книга классикой.

        Args:
            current_year: Текущий год для сравнения.

        Returns:
            True, если книга старше 50 лет, иначе False.

        Raises:
            ValueError: Если текущий год меньше года издания книги.

        Examples:
            >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
            >>> book.is_classic(2024)
            True
        """
        if current_year < self.year:
            raise ValueError("Текущий год не может быть меньше года издания книги")
        return current_year - self.year > 50


class Smartphone(ABC):
    """
    Класс, представляющий смартфон.

    Attributes:
        brand (str): Бренд смартфона.
        model (str): Модель смартфона.
        battery_capacity (int): Ёмкость аккумулятора в мАч.
    """

    def __init__(self, brand: str, model: str, battery_capacity: int) -> None:
        """
        Инициализация экземпляра класса Smartphone.

        Args:
            brand: Бренд смартфона. Не может быть пустой строкой.
            model: Модель смартфона. Не может быть пустой строкой.
            battery_capacity: Ёмкость аккумулятора. Должна быть положительной.

        Raises:
            ValueError: Если бренд, модель пусты или ёмкость аккумулятора некорректна.

        Examples:
            >>> phone = Smartphone("Apple", "iPhone 14", 3279)
            >>> phone.model
            'iPhone 14'
        """
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        if not model:
            raise ValueError("Модель не может быть пустой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Ёмкость аккумулятора должна быть положительным целым числом")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    def get_full_name(self) -> str:
        """
        Возвращает полное название смартфона.

        Returns:
            Строка с полным названием.

        Examples:
            >>> phone = Smartphone("Samsung", "Galaxy S23", 3900)
            >>> phone.get_full_name()
            'Samsung Galaxy S23'
        """
        return f"{self.brand} {self.model}"

    def estimate_battery_life(self, screen_time_hours: float) -> float:
        """
        Оценивает время работы батареи.

        Args:
            screen_time_hours: Среднее время использования экрана в часах в день.

        Returns:
            Оценочное время работы в днях.

        Raises:
            ValueError: Если время использования экрана не положительное.

        Examples:
            >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 5000)
            >>> round(phone.estimate_battery_life(5.0), 1)
            3.3
        """
        if screen_time_hours <= 0:
            raise ValueError("Время использования экрана должно быть положительным")
        # Предполагаем, что при активном использовании расходуется 300 мАч в час
        daily_consumption = screen_time_hours * 300
        return self.battery_capacity / daily_consumption


class BankAccount(ABC):
    """
    Класс, представляющий банковский счёт.

    Attributes:
        account_number (str): Номер счёта.
        owner (str): Владелец счёта.
        balance (float): Текущий баланс.
    """

    def __init__(self, account_number: str, owner: str, balance: float = 0.0) -> None:
        """
        Инициализация экземпляра класса BankAccount.

        Args:
            account_number: Номер счёта. Не может быть пустым.
            owner: Владелец счёта. Не может быть пустым.
            balance: Начальный баланс. Не может быть отрицательным.

        Raises:
            ValueError: Если номер счёта, владелец пусты или баланс отрицательный.

        Examples:
            >>> account = BankAccount("40817810099910004312", "Иван Иванов", 1000.0)
            >>> account.owner
            'Иван Иванов'
        """
        if not account_number:
            raise ValueError("Номер счёта не может быть пустым")
        if not owner:
            raise ValueError("Владелец счёта не может быть пустым")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> str:
        """
        Вносит деньги на счёт.

        Args:
            amount: Сумма для внесения. Должна быть положительной.

        Returns:
            Строка с подтверждением операции.

        Raises:
            ValueError: Если сумма не положительная.

        Examples:
            >>> account = BankAccount("40817810099910004312", "Иван Иванов", 1000.0)
            >>> account.deposit(500.0)
            'Внесено 500.0. Новый баланс: 1500.0'
        """
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")

        self.balance += amount
        return f"Внесено {amount}. Новый баланс: {self.balance}"

    def withdraw(self, amount: float) -> str:
        """
        Снимает деньги со счёта.

        Args:
            amount: Сумма для снятия. Должна быть положительной.

        Returns:
            Строка с подтверждением операции.

        Raises:
            ValueError: Если сумма не положительная или недостаточно средств.

        Examples:
            >>> account = BankAccount("40817810099910004312", "Иван Иванов", 1000.0)
            >>> account.withdraw(300.0)
            'Снято 300.0. Новый баланс: 700.0'
        """
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте")

        self.balance -= amount
        return f"Снято {amount}. Новый баланс: {self.balance}"


if __name__ == "__main__":
    # Проверка работоспособности экземпляров класса с помощью doctest
    import doctest
    doctest.testmod(verbose=True)

    # Примеры создания объектов и использования методов
    print("Примеры использования классов:")
    print("-" * 40)

    # Создание и использование книги
    try:
        book1 = Book("Война и мир", "Лев Толстой", 1869)
        print(f"Книга: {book1.get_info()}")
        print(f"Является классикой (2024): {book1.is_classic(2024)}")
    except ValueError as e:
        print(f"Ошибка при создании книги: {e}")

    print("-" * 40)

    # Создание и использование смартфона
    try:
        phone1 = Smartphone("Apple", "iPhone 15", 3349)
        print(f"Смартфон: {phone1.get_full_name()}")
        print(f"Ёмкость батареи: {phone1.battery_capacity} мАч")
        print(f"Оценка времени работы (при 6 часах экрана в день): {phone1.estimate_battery_life(6):.1f} дней")
    except ValueError as e:
        print(f"Ошибка при создании смартфона: {e}")

    print("-" * 40)

    # Создание и использование банковского счёта
    try:
        account1 = BankAccount("40817810099910004312", "Анна Петрова", 5000.0)
        print(f"Владелец счёта: {account1.owner}")
        print(f"Начальный баланс: {account1.balance}")
        print(account1.deposit(1500.0))
        print(account1.withdraw(2000.0))
    except ValueError as e:
        print(f"Ошибка при работе с банковским счётом: {e}")

    print("-" * 40)

    # Пример с ошибкой валидации
    print("Примеры ошибок валидации:")
    try:
        invalid_book = Book("", "Автор", 2024)
    except ValueError as e:
        print(f"Ошибка создания книги: {e}")

    try:
        invalid_phone = Smartphone("Brand", "", -100)
    except ValueError as e:
        print(f"Ошибка создания смартфона: {e}")

    try:
        invalid_account = BankAccount("123", "Владелец", -100)
    except ValueError as e:
        print(f"Ошибка создания счёта: {e}")