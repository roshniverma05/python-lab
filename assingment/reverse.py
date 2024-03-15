x=int(input("enter a number : "))
rev=0
temp=x
while(x>0):
    num=x%10
    rev=rev*10+num
    x=x//10
print(rev)