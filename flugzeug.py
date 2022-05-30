from vehicles import Vehicles

class Flugzeug (Vehicles):
    def __init__(self, model, price, manufactureYear, maxSpeed, maxHeigh):
        
        self.maxHeigh = maxHeigh
        self.maxSpeed = maxSpeed
        self.model = model
        self.manufactureYear = manufactureYear
        self.price = price
        

    
    def show(self):
        print(f"model - {self.model}")
        print(f"price - {self.price}$")
        print(f"manufactureYear - {self.manufactureYear}")
        print(f"maxSpeed - {self.maxSpeed} km/h")
        print(f"maxHeigh - {self.maxHeigh} m")
    