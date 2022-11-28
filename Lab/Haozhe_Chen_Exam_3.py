###         Haozhe Chen

#  Question: 1
class vehicle:
    def __init__(self,numPassenger,manufacturer,numWheels):
        self.numPassenger = numPassenger
        self.manufacturer = manufacturer
        self.numWheels = numWheels


class automobile(vehicle):
    def __init__(self, numPassenger, manufacturer, numWheels,mpg,model,numDoors):
        super().__init__(numPassenger, manufacturer, numWheels)
        self.mpg = mpg
        self.model = model
        self.numDoors = numDoors

    def printInfo(self):
        print("====Vehicle Info====")
        print(f"Passengers(max): {self.numPassenger}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Wheels: {self.numWheels}")
        print(f"MPG: {self.mpg}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.numDoors}")
        print(" ")


class sedan(automobile):
    def __init__(self, numPassenger, manufacturer, numWheels, mpg, model, numDoors,typ,numCylinder,horsepower):
        super().__init__(numPassenger, manufacturer, numWheels, mpg, model, numDoors)
        self.type = typ
        self.numCylinder = numCylinder
        self.horsepower = horsepower

    def printInfo(self):
        print("====Vehicle Info====")
        print(f"Passengers(max): {self.numPassenger}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Wheels: {self.numWheels}")
        print(f"MPG: {self.mpg}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.numDoors}")
        print(f"Type: {self.type}")
        print(f"Num Cylinder: {self.numCylinder}")
        print(f"Horse Power: {self.horsepower}")
        print(" ")


class truck(automobile):
    def __init__(self, numPassenger, manufacturer, numWheels, mpg, model, numDoors,typ,numAxels,maxTowPayload):
        super().__init__(numPassenger, manufacturer, numWheels, mpg, model, numDoors)
        self.type = typ
        self.numAxels = numAxels
        self.maxTowPayload = maxTowPayload

    def printInfo(self):
        print("====Vehicle Info====")
        print(f"Passengers(max): {self.numPassenger}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Wheels: {self.numWheels}")
        print(f"MPG: {self.mpg}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.numDoors}")
        print(f"Type: {self.type}")
        print(f"Number of Axels: {self.numAxels}")
        print(f"Max Tow Pay Load: {self.maxTowPayload}")
        print(" ")


class twoWheeler(vehicle):
    def __init__(self, numPassenger, manufacturer, numWheels, model, weight):
        super().__init__(numPassenger, manufacturer, numWheels)
        self.model = model
        self.weight = weight

    def printInfo(self):
        print("====Vehicle Info====")
        print(f"Passengers(max): {self.numPassenger}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Wheels: {self.numWheels}")
        print(f"MPG: {self.mpg}")
        print(f"Model: {self.model}")
        print(f"Weight: {self.weight}")
        print(" ")


class motorcycle(twoWheeler):
    def __init__(self, numPassenger, manufacturer, numWheels, model, weight,typ,mpg,horsepower):
        super().__init__(numPassenger, manufacturer, numWheels, model, weight)
        self.type = typ
        self.MPG = mpg
        self.horsepower = horsepower

    def printInfo(self):
        print("====Vehicle Info====")
        print(f"Passengers(max): {self.numPassenger}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Wheels: {self.numWheels}")
        print(f"MPG: {self.mpg}")
        print(f"Model: {self.model}")
        print(f"Weight: {self.weight}")
        print(f"Type: {self.typ}")
        print(f"MPG: {self.MPG}")
        print(f"Horse Power: {self.horsepower}")
        print(" ")


class bicycle(twoWheeler):
    def __init__(self, numPassenger, manufacturer, numWheels, model, weight,hasGears,hasSuspensions,wheelSize):
        super().__init__(numPassenger, manufacturer, numWheels, model, weight)
        self.hasGears = hasGears
        self.hasSuspensions = hasSuspensions
        self.wheelSize = wheelSize

    def printInfo(self):
        print("====Vehicle Info====")
        print(f"Passengers(max): {self.numPassenger}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Wheels: {self.numWheels}")
        print(f"MPG: {self.mpg}")
        print(f"Model: {self.model}")
        print(f"Weight: {self.weight}")
        print(f"Gears: {self.hasGears}")
        print(f"Suspensions: {self.hasSuspensions}")
        print(f"Wheel Size: {self.wheelSize}")
        print(" ")


""

# Question: 2
#During the diagram. The class named vehicle is the parent of the classes named Automobile and TwoWheeler. 
#Also, the classes named Sedan and Truck are the children of Automobile.
#The classes named Motorcycle and bicycle are the children of TowWheeler.

""

# Question: 3

import random
class customer:
    def __init__(self,amount):
        self.amount = amount

    def discountReached(self):
        discount = self. amount / 100
        dis = int(discount)*10
        return dis
    
    def __str__(self):
        print("Hi, this is xxxx market, in our system you already purchase",self.amount,"$ commodity.")
        print("During our discount, you could get",self.discountReached(),"$ as discount when you come here next time.")
        return " "
print(customer(random.randint(0000,10000)))