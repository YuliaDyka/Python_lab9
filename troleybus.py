from vehicles import Vehicles

class Troleybus (Vehicles):
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, power: int):
        
        self.power = power 
        self.max_speed = max_speed
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price
        
    def __str__(self):
        return f"model - {self.model}\nprice - {self.price}$\nmanufacture year - {self.manufacture_year}\nmax speed - {self.max_speed} km/h\npower - {self.power} W"
    