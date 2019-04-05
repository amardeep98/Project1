def count(lst):
    even=0
    odd=0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd

lst=[2,87,56,45,77,88,564,23]
even,odd=count(lst)
print("Even:{} and odd:{}".format(even,odd))
