for x in range(500,1000):
    # temp=x
    # rev=0
    # while(x>0):
    #     num=x%10
    #     rev=rev*10+num
    #     x=x//10
    # print(rev)
    # if(temp==rev):
    #     print("entered number is a palindrome", x)
    # else:
    #     print("not a palindrome")
    reverse = ''    
    str_x = str(x)
    for j in str_x:
        reverse = j + reverse   

    if ( str_x == reverse):
        print("yes" , str_x)    