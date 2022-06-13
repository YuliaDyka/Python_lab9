from vehicle import Vehicle

class Tram (Vehicle):
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, passenger_car_count: int):
        
        self.passenger_car_count = passenger_car_count
        self.max_speed = max_speed
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price
        
    def __str__(self):
        return super().__str__() + f"passenger car count - {self.passenger_car_count}"