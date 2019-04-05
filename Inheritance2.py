class Base:
    def greet(self):
        print("Hello Base")

class Derived(Base):
    pass                                                                     #for DRY

b1=Base()
b1.greet()

d1=Derived()
d1.greet()
print(help(Derived))
