x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(x[0])):
    for j in range(len(y[0])):
        for k in range(len(result[0])):
            result[i][j] += x[i][j] * y[i][j] 
print(result)            