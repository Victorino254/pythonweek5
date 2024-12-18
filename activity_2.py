# Activity 2: Polymorphism Challenge!

# Base class for Vehicles
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Derived class for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived class for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
