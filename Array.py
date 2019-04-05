from array import *
arr1=array('i',[4,87,5,87,9])
print(arr1.buffer_info())

arr2=array(arr1.typecode,(a*a for a in arr1))
for i in range(len(arr2)):
    print(arr2[i]," ",end='')
print()

arr3=array('u',['a','g','y','o'])
for e in arr3:
    print(e,end=" ")
print()

arr1.reverse()
for k in arr1:
    print(k,' ',end="")
print()

arr4=arr1
arr5=arr1+arr4
print(arr4)
print(arr5)
