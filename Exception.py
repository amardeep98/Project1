#Program to handle Exception
try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    if b==0:
        raise ZeroDivisionError("You cannot divide by zero")
    result=a/b
except ZeroDivisionError as ze:
    print(ze)
else:
    print("Result is",result)
finally:
    print("Addition=",a+b)
