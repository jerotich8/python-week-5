# Base class
class Vehicle:
    def move(self):
        return "This vehicle moves."

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving"

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying"

# Derived class: Boat
class Train(Vehicle):
    def move(self):
        return "Running on tracks"

# Function demonstrating polymorphism
def define_movement(vehicle):
    print(vehicle.move())

# Creating objects
car = Car()
plane = Plane()
train = Train()

# Using polymorphism
vehicles = [car, plane, train]
for vehicle in vehicles:
    define_movement(vehicle)
