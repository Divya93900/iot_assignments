a=int(input("enter the marks:"))
b=int(input("enter the marks:"))
c=int(input("enter the marks:"))
avg=((a+b+c)/3)
if(90<avg<100):
    print("grade A")
elif(80<avg<89 ):
    print("grade b")
elif(70<avg<79 ):
    print("grade c")
elif(60<=avg<69):
    print("grade d")    
else:
    print("fail")

