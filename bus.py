from vehicles import Vehicles

class Bus (Vehicles):
    
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, passenger_count: int):
        
        self.passenger_count = passenger_count
        self.model = model
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed
        self.price = price
       
    def __str__(self):
        return f"model - {self.model}\nprice - {self.price}$\nmanufacture year - {self.manufacture_year}\nmax speed - {self.max_speed} km/h\npassenger count - {self.passenger_count}"
    