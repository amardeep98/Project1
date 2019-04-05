from ast import literal_eval
nmbr=input("Enter number:")
def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError,SyntaxError):
        return str

if get_type(nmbr)==int:
    mltr=1
    while(mltr<=10):
        print(nmbr,'x',mltr,'=',int(nmbr)*int(mltr))
        mltr+=1

elif get_type(nmbr)==float:
    mltr=1
    while(mltr<=10):
        print(nmbr,'x',float(mltr),'=',float(nmbr)*float(mltr))
        mltr+=1

else:
    print("Please enter a number:")