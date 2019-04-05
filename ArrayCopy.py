from numpy import *
arr1=array([2,3,4,56,6])
arr2=arr1.view()        #shallow copy
arr1[1]=7
print(arr1,"  id=",id(arr1))
print(arr2,"  id=",id(arr2))

arr3=array([4,45,56,6,2])
arr4=arr3.copy()        #deep copy
arr3[2]=4
print(arr3,"  id=",id(arr3))
print(arr4,"  id=",id(arr4))