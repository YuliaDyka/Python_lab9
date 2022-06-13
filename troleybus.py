from vehicle import Vehicle

class Troleybus (Vehicle):
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, power: int):
        
        self.power = power 
        self.max_speed = max_speed
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price
        
    def __str__(self):
          return super().__str__() + f"power - {self.power} W"
    
