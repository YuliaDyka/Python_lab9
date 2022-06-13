from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def __init__(self):
        self.model = ""
        self.price = 0
        self.manufacture_year = 0
        self.max_speed = 0

    def __str__(self):
            return f"model - {self.model}\nprice - {self.price}$\nmanufacture year - {self.manufacture_year}\nmax speed - {self.max_speed} km/h\n"

