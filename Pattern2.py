for i in range(1,6):
    for j in range(1,10):
        if j>=7-i and j<=3+i:
            print(" ",end="")
        else:
            print("*",end="")
    print()            
