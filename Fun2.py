def update(x):
    print("id in function before changing value",id(x))   #same
    x=8
    print("id in function after changing value:",id(x))   #different
    print("x=",x)

a=10
print("id before calling function:",id(a))                 #same
update(a)
print("a=",a)            #original value doesn't change cuz integer,string are immutable
