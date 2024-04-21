def fun(n):
    fact=1
    for num in range(1,n+1):
        fact=num*fact
    print(fact)
n=int(input("enter the number"))    
#fun(n)
for num in range(1,n+1):
    fun(num)
