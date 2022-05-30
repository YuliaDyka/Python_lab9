from vehicles import Vehicles

class Car (Vehicles):
    def __init__(self, model, price, manufactureYear, maxSpeed, fuelType):
        self.fuelType = fuelType
        self.model = model
        self.manufactureYear = manufactureYear
        self.price = price
        self.maxSpeed = maxSpeed

    
    def show(self):
        print(f"model - {self.model}")
        print(f"price - {self.price}$")
        print(f"manufactureYear - {self.manufactureYear}")
        print(f"maxSpeed - {self.maxSpeed} km/h")
        print(f"fuelType - {self.fuelType}")