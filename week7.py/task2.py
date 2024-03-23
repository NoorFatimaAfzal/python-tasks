#getting matrix as input from user
matrix = []
for i in range(2):
   row = []
   for j in range(2):
      element = int(input("enter element: "))
      row.append(element)
   matrix.append(row)
print(f"the given matrix is: ",matrix)

# now im going to find determinent og given matrix
det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
print(f"the determunent of given matrix is: ",det)

# now im going to find adjoint og given matrix
entry=matrix[1][1]
matrix[1][1]=matrix[0][0]
matrix[0][0]=entry
matrix[0][1]=matrix[0][1]*-1
matrix[1][0]=matrix[1][0]*-1
print(f"the adjoint of given matrix is: ",matrix)

# now im going to find adjoint og given matrix

try:
    for i in range(len(matrix)):    
        for j in range(len(matrix[i])):  
            matrix[i][j]=matrix[i][j]/det
            matrix[i][j] += 1
    print(f"the iverse of given matrix is: ",matrix)
except Exception as error:
    print(error)
else:
    print("inverse found succesfully ! ")