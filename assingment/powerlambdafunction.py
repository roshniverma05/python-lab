x = int(input("Enter the Total Number of Terms: "))
fun = lambda x: 2 ** x
for i in range(x):
    print("2 raised to the power ", i, " is ", fun(i))



