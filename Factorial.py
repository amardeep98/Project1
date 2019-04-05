"""
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

"""


def sum(m):
    if(m==1):
        return 1
    return m+sum(m-1)

num=int(input("Enter a natural number:"))
if num<1:
    print("Please enter a natural number")
    num=int(input("Enter a natural number:"))
    print(sum(num))

else:
    print(sum(num))
