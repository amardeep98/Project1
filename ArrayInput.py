from array import *
arr1=array('i',[])
n=int(input("Enter the size of the array:"))
for i in range(n):
    x=int(input("Enter the next value:"))
    arr1.append(x)
print("The array elements are:")
for i in range(n):
    print(arr1[i]," ",end="")
print()

k = int(input("Enter the element to be searched:"))
print("The index is:",arr1.index(k))
