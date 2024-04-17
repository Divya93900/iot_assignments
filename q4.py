num1=int(input("enter the integer:"))
num2 =int(input("enter the integer:"))
num3=int(input("enter the integer:"))
if(num1>num2 and num1>num3):
    print("num1 is greater")
elif(num2>num3 and num2>num1):
    print("num2 is greater")
elif(num3>num1 and num3>num2):
    print("num3 is greater")
elif(num1==num2 and num3<num1):
    print(" num1 and num2 equal num3 less")
elif(num1==num3 and num2<num1):
    print("num1 and num3 equal num2 less")
elif(num2==num3 and num1<num2):
    print("num2 and num3 equal num1 less")
elif(num1==num2 and num3>num1):
    print(" num1 and num2 equal num3 greater")
elif(num1==num3 and num2>num1):
    print("num1 and num3 equal num2 greater")
elif(num2==num3 and num1>num2):
    print("num2 and num3 equal num1 greater")    
else:
    print("all are equal")
        


