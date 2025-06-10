from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        print("Making sound")

    @staticmethod
    def can_eat():
        print("Can eat")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cow(Animal):

    def make_sound(self):
        print("amba")

dog = Dog("Alseshan")
dog.make_sound()
dog.can_eat()
print(f"dog name is {dog.name}")
cow = Cow("Lakshmi")
print(cow.name)
cow.make_sound()
