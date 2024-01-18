# Create a Python class called “Car” with attributes like make, model, and year. Then, create an object of the “Car” class and print its details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_details(self):
        return f"{self.year} {self.make} {self.model}"
carObj = Car(make="Toyota", model="Supra", year=2023)
print("Car Details:")
print(carObj.get_details())
