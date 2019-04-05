def update(lst):
    print("id before updation:",id(lst))     #same
    lst[2]=54
    print("id after updation:",id(lst))      #same
    print("list values:",lst)

lst=[10,20,30,48]
print("id before function call:",id(lst))     #same
print("list values before function call:",lst)
update(lst)
print("list values after function call:",lst)