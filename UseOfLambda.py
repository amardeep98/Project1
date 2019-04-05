from functools import *

lst=[3,8,7,5,6,12,15,20]
evens=list(filter(lambda a:a%2==0,lst))
print(evens)

doubles=tuple(map(lambda a:a*2,evens))
print(doubles)

sum=reduce(lambda a,b:a+b, doubles)
print(sum)