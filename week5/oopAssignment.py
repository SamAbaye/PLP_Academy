# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗,
#  while Plane.move() prints "Flying" ✈️).
class House:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def move(self):
        print("Moving in the house")

# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗,
#  while Plane.move() prints "Flying" ✈️).
class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")
