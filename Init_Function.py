class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def __del__(self):
        print("Object deleted")

    def config(self):
        print("cpu=",self.cpu,"and ram=",self.ram)

com1=Computer('i5',16)
com2=Computer('Ryzen 3',8)

com1.config()
com2.config()
Computer.config(com1)



"""
def __del__(self):                  #deletes the object after entire program has executed
    print('object deleted')

if n objects are created, __del__() runs n times    
"""
