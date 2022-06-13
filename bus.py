from vehicle import Vehicle

class Bus (Vehicle):
    
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, passenger_count: int):        
        self.passenger_count = passenger_count
        self.model = model
        self.price = price
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed
        # super().__init__(model, price, manufacture_year, max_speed)
    
    def __str__(self):
        return super().__str__() + f"passenger count - {self.passenger_count}"