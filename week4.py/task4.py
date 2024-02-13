row_1=input("enter elements of row 1 separated by space")
row_2=input("enter elements of row 2 separated by space")
row_3=input("enter elements of row 3 separated by space")
make_list1=row_1.split()
make_list2=row_2.split()
make_list3=row_3.split()
matrix=[]
matrix.append(make_list1)
matrix.append(make_list2)
matrix.append(make_list3)
print(matrix)
new_matrix=[[0,0,0],[0,0,0],[0,0,0]]
new_matrix[0][0]=matrix[0][0]
new_matrix[0][1]=matrix[1][0]
new_matrix[0][2]=matrix[2][0]

new_matrix[1][0]=matrix[0][1]
new_matrix[1][1]=matrix[1][1]
new_matrix[1][2]=matrix[2][1]

new_matrix[2][0]=matrix[0][2]
new_matrix[2][1]=matrix[1][2]
new_matrix[2][2]=matrix[2][2]
print(new_matrix)
