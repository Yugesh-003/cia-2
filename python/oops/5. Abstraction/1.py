from abc import ABC, abstractmethod

# Abstract class
class Fruit(ABC):
    @abstractmethod
    def taste(self):
        pass

# Concrete class 1
class Apple(Fruit):
    def taste(self):
        return "Sweet"

# Concrete class 2
class Orange(Fruit):
    def taste(self):
        return "Sour"

# Creating objects
apple = Apple()
orange = Orange()

# Accessing methods
print("Apple Taste:", apple.taste())
print("Orange Taste:", orange.taste())
