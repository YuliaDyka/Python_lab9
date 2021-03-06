from car import Car
from bus import Bus
from flugzeug import Flugzeug
from troleybus import Troleybus
from tram import Tram

print ("\n------- Lab9 --------\n")

print ("\n------- Car --------\n")

car = Car("Ford", 2500, 2015, 200, "benzin")
car.show()

print ("\n------- Bus --------\n")

bus = Bus("Bogdan", 5000, 2016, 80, 23)
bus.show()

print ("\n------- Flugzeug --------\n")

flugzeug = Flugzeug("Boing-325", 250000, 2010, 900, 10000)
flugzeug.show()

print ("\n------- Troleybus --------\n")

troleybus = Troleybus("IPN-123", 10000, 2005, 60, 5000)
troleybus.show()

print ("\n------- Tram --------\n")

tram = Tram(f"RP-53", 12000, 2011, 30, 2)
tram.show()
print ("\n")