matrix=[
    [1,1],
    [1,3]
]
det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

entry=matrix[1][1]
matrix[1][1]=matrix[0][0]
matrix[0][0]=entry
print(matrix)

try:
    for i in range(len(matrix)):    
        for j in range(len(matrix[i])):  
            matrix[i][j]=matrix[i][j]/det
            matrix[i][j] += 1
    print(matrix)
except Exception as error:
    print(error)