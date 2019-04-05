class Car:
    def __init__(self,pickup,mileage):
        self.pickup=pickup
        self.mileage=mileage

    def disp(self):
        print("Pickup and Mileage=",self.pickup,self.mileage)


class Verna(Car):
    def __init__(self,pickup,mileage):
        super().__init__(pickup,mileage)                                         #calling base class constructor

    def disp(self):
        print("Mileage and Pickup=",self.mileage,self.pickup)                    #method overriding

verna1=Verna(70,14)
print(verna1.pickup)
verna1.disp()
