class Car:
    wheels=4
    def __init__(self,color,types):
        self.color=color
        self.types=types

polo=Car("Red","HB")
Dzire=Car("White","Sedan")
print("no. of wheels=",Car.wheels)
print("{} car in {} colour is Polo".format(polo.types,polo.color))
