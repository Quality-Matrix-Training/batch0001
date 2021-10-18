from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def show(self):
        print("abstract class")

class Car1(Vehicle):
    def show(self):
        print("car1")

class Car2(Vehicle):
    def show(self):
        print("Car2")
    # def show(self):
    #     print("car2")



C1 = Car1()
C1.show()
Car2().show()