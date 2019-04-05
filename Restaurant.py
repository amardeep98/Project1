#program for taking orders and billing in a Restaurant
from array import *
f=open('Menu.txt','w',encoding='utf-8')
f.write('          RESTAURANT NAME               \n')
f.write("               MENU                    \n")
f.write("S.no.      ITEM               Price in $\n")
f.write("1          Salmon                3      \n")
f.write("2          Onion Fry             4      \n")
f.write("3          Minced Mutton         6      \n")
f.write("4          Stuffed Naan          1      \n")
f.write("5          Diet Coke             2      \n")
mlist=['Salmon','Onion Fry','Minced Mutton','Stuffed Naan','Diet Coke']                #mlist=list of items
plist=[3,4,6,1,2]                                                                      #plist=price list according to mlist
print("***********************************************\n")
print("YOUR ORDER HERE")
print("Press * after ordering")
item=array('i',[])                                                    #'item' array for storing ordered item nos.
qnt=array('i',[])                                                     #'qnt' array for storing quantity for each ordered item
item.append(int(input("Enter Item no. :")))
qnt.append(int(input("Enter quantity for the item :")))
while True:
    temp=(input("Enter next Item no. :"))
    if temp!='*':
        item.append(int(temp))
    else:
        item.append(111)                                              #'111' in the array means no items ordered further
        break
    qnt.append(int(input("Enter quantity for the item :")))

def bill(item,qnt):                                                #function for billing
    count=0                                                        #for array index
    tempItem=item[count]                                           #for storing current indexed item no. temporarily
    total=0                                                        #'total' for total amount
    while tempItem!=111:
        tempQnt=qnt[count]
        total+=plist[tempItem-1]*tempQnt
        count+=1
        tempItem=item[count]
    return total


price=bill(item,qnt)
print("\n**************************************")
print("\n             RESTAURANT NAME             ")
print("\n              YOUR ORDERS               \n ")
orderc=0                                                                        #order count
oitem=item[orderc]
print("S.no\tItem\tQuantity\tPrice\n")
while oitem!=111:
    oqnt=qnt[orderc]
    print(orderc+1,'\t',mlist[oitem-1],'\t',oqnt,'\t',oqnt*plist[oitem-1])
    orderc+=1
    oitem=item[orderc]

print("\nTotal amount=",price,"$")
print("***********Thank You*************")
print("***********Visit Again***********")
