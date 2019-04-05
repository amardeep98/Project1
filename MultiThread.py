from time import sleep
from threading import *

class A(Thread):
    def run(self):
        for i in range(0,5):
            print("hello")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(0,5):
            print("hi")
            sleep(1)

t1=A()
t2=B()
t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()
print("Bye")
