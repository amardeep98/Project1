import os
os.system('cls')

class Enc:
    num1=3
    _num2=5   #kind of protected
    __num3=6  #private

    def sets(self):
        self.__num3=24
        return self.__num3

    def pub(self):
        print("Public method")

    def __pri(self):
        return self.__num3

    def _pro(self):
        print("Protected method")

    def gets(self):
         return self.__pri()


obj=Enc()
print(obj.num1)
print(obj._num2)
print(obj.gets())
print(obj.sets())
obj._pro()
obj.pub()
