from numpy import *
arr=([2,3,4],[8,9,6],int)
print(arr[0][2])

arr1=array([1,2,3,4])
print(arr1.dtype,"\n")

arr2=linspace(0,50,26)   #50 parts if not specified
print(arr2,"\n")

arr3=arange(1,30,2)      #skips 2 values
print(arr3,"\n")

arr4=logspace(1,40,5)
print(arr4)
print('%.2f'%arr4[4],"\n")

arr5=zeros(5)
print(arr5)

arr6=ones(6,int)
print(arr6)

arr7=arr6+5
print(arr7)

arr8=arr7+arr6
print(arr8)