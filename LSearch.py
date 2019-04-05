pos=-1
def search(lst,n):
    i=0
    while i<len(lst):
        if lst[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False

lst=[3,4,5,6,77,8]
n=3
if search(lst,n)==True:
    print("Found at",pos)
else:
    print("not found")