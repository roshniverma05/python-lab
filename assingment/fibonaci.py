'''x=int(input("enter the range to print a series : "))
a=int(input("enter first number : "))
b=int(input("enter second number : "))
temp=b
count=1
while(count<=x):
    print(temp,end=" ")
    count+=1
    a,b=b,temp
    temp=a+b
print()   
'''
x=int(input("enter the range to print a series : "))
a=int(input("enter first number : "))
b=int(input("enter second number : "))
for i in range(0,x):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    

