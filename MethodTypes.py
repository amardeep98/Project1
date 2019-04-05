class Student:
    clg="rce"

    def __init__(self,m1,m2,m3):    #instance method
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod                    #decorator
    def getclg(cls):                #class method
        return cls.clg

    @staticmethod                   #decorator
    def info():                     #static method
        print("Doesn't use class or instance variables")

s1=Student(77,33,76)
s2=Student(45,56,87)

print(s1.avg())
print(Student.getclg())
Student.info()