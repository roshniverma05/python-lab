x=int(input("enter a number : "))
temp=x
rev=0
while(x>0):
    num=x%10
    rev=rev*10+num
    x=x//10
print(rev)
if(temp==rev):
 print("entered number is a palindrome")
else:
   print("not a palindrome")