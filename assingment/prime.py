x = int(input("enter a number"))

for n in range(2, x-1):
    if(x % n == 0):
        print('not a prime')
        break
    else: print('prime')