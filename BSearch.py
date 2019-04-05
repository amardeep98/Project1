pos=-1
def bsearch(lst,n):
    l = 0
    u=len(lst)
    while l<=u:
        mid=(l+u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if(lst[mid]<n):
                l=mid
            else:
                u=mid
    return False


lst=[3,4,5,7,8,9]
n=9
if bsearch(lst,n)==True:
    print("Found at",pos)
else:
    print("not found")
