k=0
for i in range(1,8):
    if i<=4:
        k+=1
    else:
        k-=1
    for j in range(1,8):
        if j>=5-k and j<=3+k:
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
This is a document type string called DocString.
It can expand up to multiple lines.
But it is not called multi line string.
"""
