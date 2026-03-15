if __name__ == "__main__":
    # Write your solution here
    pass
class Animal:
    def __init__(self, name: str, age: int, species: str) -> None:
        self.name = name
        self.age = age
        self._species = species
    def __str__(self) -> str:
        return f"{self.name} ({self._species}), возраст: {self.age}"

    def __repr__(self) -> str:
        return f"Animal(name='{self.name}', age={self.age}, species='{self._species}')"
    def make_sound(self) -> str:
        return "Издаёт звук"
    def move(self) -> str:
        return "Животное передвигается"
class Bird(Animal):
    def __init__(self, name: str, age: int, species: str, can_fly: bool, wing_span: float) -> None:
        super().__init__(name, age, species)
        self.can_fly = can_fly
        self._wing_span = wing_span
    def __str__(self) -> str:
        base_info = super().__str__()
        flight_info = "летает" if self.can_fly else "не летает"
        return f"{base_info}, {flight_info}, размах крыльев: {self._wing_span}м"
    def __repr__(self) -> str:
        return (f"Bird(name='{self.name}', age={self.age}, species='{self._species}', "
                f"can_fly={self.can_fly}, wing_span={self._wing_span})")
    def make_sound(self) -> str:
        return "Чирик-чирик"
    def build_nest(self) -> str:
        return f"{self.name} строит гнездо"
if __name__ == "__main__":
    generic_animal = Animal("Барсик", 3, "Кошка")
    print(generic_animal)
    print(repr(generic_animal))
    print(generic_animal.make_sound())
    print(generic_animal.move())
    print("-" * 30)
    bird = Bird("Кеша", 2, "Волнистый попугайчик", True, 0.15)
    print(bird)
    print(repr(bird))
    print(bird.make_sound())
    print(bird.move())
    print(bird.build_nest())