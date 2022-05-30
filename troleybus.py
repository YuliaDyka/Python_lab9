from vehicles import Vehicles

class Troleybus (Vehicles):
    def __init__(self, model, price, manufactureYear, maxSpeed, power):
        
        self.power = power 
        self.maxSpeed = maxSpeed
        self.model = model
        self.manufactureYear = manufactureYear
        self.price = price
        

    
    def show(self):
        print(f"model - {self.model}")
        print(f"price - {self.price}$")
        print(f"manufactureYear - {self.manufactureYear}")
        print(f"maxSpeed - {self.maxSpeed} km/h")
        print(f"power - {self.power} W")