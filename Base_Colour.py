# Define a class attribute “color” with a default value white. i.e., Every Vehicle should be white.
class Vehicle:
    color = "white"
    def __init__(self, capacity):
        self.capacity = capacity
    def calcFare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)
    def calcFare(self):
        base_fare = super().calcFare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

vehicle1 = Vehicle(50)
bus1 = Bus(50)

print(f"Vehicle Fare: ${vehicle1.calcFare()}, Color: {vehicle1.color}")
print(f"Bus Fare: ${bus1.calcFare()}, Color: {bus1.color}")
