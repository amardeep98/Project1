class Person:
    def __init__(self):
        self.name="Amar"
        self.age=21

    def compare(self,other) :
        if self.age==other.age:
            return True
        else:
            return False

p1=Person()
p2=Person()
print(id(p1))
print(id(p2))

p2.age=20
if p1.compare(p2):
    print("Same")
else:
    print("Different")
