class Car:
    wheels=4                   #class variable

    def __init__(self):
        self.mil=12            #instance variable
        self.brnd="BMW"        #instance variable


c1=Car()
c2=Car()
c1.mil=10
print(c1.mil," ",c1.brnd)
print(c2.mil," ",c2.brnd)

Car.wheels=5
print(c1.wheels)
print(c2.wheels)