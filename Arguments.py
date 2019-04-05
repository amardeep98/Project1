def add(a,b):
    c=a+b
    print("sum=",c)

add(3,8)

def person(name,age):
    print("name=",name)
    print("age=",age)

person(age=20,name='Amar')              #keyword

def pen(type,cost=5):
    print("type=",type)
    print("cost=",cost)

pen('ball')

def add(a, *b):                        #Variable Length
    print(a)
    print(b)
    
add(4,5,8,9,6)
