f=lambda num,i:num**i

num=int(input("Enter the number:"))
rng=int(input("Enter the range:"))
for i in range(0,rng+1):
    print(f(num,i))