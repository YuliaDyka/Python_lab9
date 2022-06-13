from vehicle import Vehicle

class Car (Vehicle):
    def __init__(self, model: str, price: int, manufacture_year: int, max_speed: int, fuel_type: str):
        self.fuel_type = fuel_type
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f"fuel type - {self.fuel_type}"