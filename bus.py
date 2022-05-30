from vehicles import Vehicles

class Bus (Vehicles):
    
    def __init__(self, model, price, manufactureYear, maxSpeed, passengerCount):
        
        self.passengerCount = passengerCount
        self.model = model
        self.manufactureYear = manufactureYear
        self.maxSpeed = maxSpeed
        self.price = price
       

    
    def show(self):
        print(f"model - {self.model}")
        print(f"price - {self.price}$")
        print(f"manufactureYear - {self.manufactureYear}")
        print(f"maxSpeed - {self.maxSpeed} km/h")
        print(f"passengerCount - {self.passengerCount}")