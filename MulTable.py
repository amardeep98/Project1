n=int(input("Enter the range:"))           #taking input
i=1                                     #counter for  table of different nos.
while(i<=n):
    print("Printing the table of",i)    #indicates the table to be printed
    j=1
    while(j<=10):                       #10 rows for each table
        print(i,"x",j,"=",i*j)
        j+=1                            #updation of rows
    i+=1                                #updation of table no.
    print()

