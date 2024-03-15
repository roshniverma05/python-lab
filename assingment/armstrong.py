x=int(input("enter a number :"))
temp=x
sum=0
while(x>0):
    dig=x%10
    sum=sum+dig**3
    x=x//10
if(temp==sum):
    print(temp, " is an  armstrong")
else:
    print(temp," is not an armstrong")        
