class Book:
    """
    Базовый класс Книги.
    """
    def init(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"Книга {self.name}. Автор {self.author}"

    def repr(self):
        return f"{self.class.name}({self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Бумажная книга.
    """
    def init(self, name: str, author: str, pages: int):
        super().init(name, author)
        self.pages = pages  # используем setter для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def repr(self):
        return f"{self.class.name}({self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """
    Аудиокнига.
    """
    def init(self, name: str, author: str, duration: float):
        super().init(name, author)
        self.duration = duration  # используем setter для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = float(value)

    def repr(self):
        return f"{self.class.name}({self.name!r}, author={self.author!r}, duration={self.duration})"