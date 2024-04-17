def fact(n):
    #factorial=1
    if(n==1 or n==0):
        return 1
    else:
        return (n*fact(n-1))    
    
    
    #print(fact)
n=int(input("enter the number"))    
f=fact(n)
print(f)
#fun(5)       
 