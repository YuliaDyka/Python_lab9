class Vehicles:
    def __init__(self):
        self.model = ''
        self.price = 0
        self.manufactureYear = 0
        self.maxSpeed = 0



    def show(self):
        print(f"model - {self.model}")
        print(f"price - {self.price}$")
        print(f"manufactureYear - {self.manufactureYear}")
        print(f"maxSpeed - {self.maxSpeed} km/h")