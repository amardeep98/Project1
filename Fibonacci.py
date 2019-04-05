def Fibo(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        s=a+b
        print(s,end=" ")
        a,b=b,s

i=int(input("Enter the no.of terms:"))
Fibo(i)

#for printing upto some number,another method
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()

fib(1000)
