#que 2

l1=[1,3,4,2]
l2=[3,2,2,2]
sum=[0,0,0,0]
for i in range(l1[0]):
   for j in range(l2[0]):
      sum = l1[i] + l2[j]
print(sum)        


#que 1
x=int(input("enter a number : "))
num=1
for i in range(x+1):
    for j in range(1,i+1):
        print(j,end=" ")
    
    print()  
    