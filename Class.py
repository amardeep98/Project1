class Operate:
    x="Hello"
    def add(self,a,b):
        print(a+b)


op=Operate()
op.add(4,5)
print(Operate.x)
op.__class__.x="Bye"
print(Operate.x)

"""
we can't change the class values through instance
only instance values can be changed through instance
To change class values through instance,we use-
        object_name.__class__.variable_name="updated value"
"""
