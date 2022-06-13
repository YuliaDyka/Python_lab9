from vehicle import Vehicle

class Flugzeug (Vehicle):
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, max_heigh: int):
        
        self.max_heigh = max_heigh
        self.max_speed = max_speed
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price
        
    def __str__(self):
        return super().__str__() + f"max heigh - {self.max_heigh} m"