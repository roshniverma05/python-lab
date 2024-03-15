#1
'''
x=int(input("enter a number : "))
for i in range(0,x):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
'''

#2
'''
x=int(input("enter a number : "))
for i in range(x,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
'''    

#3
'''
x=int(input("enter a number : "))
k=x-1
for i in range(0,x):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")   
'''

#4
'''
x=int(input("enter number of rows : "))
num=1
for i in range(x):
    for j in range(i+1):
        print(num,end=" ")
    num+=1
    print()    
'''

#5 pascal's triangle
'''
rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()
'''

#6 flyodd's triangle
'''
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()
'''
    
