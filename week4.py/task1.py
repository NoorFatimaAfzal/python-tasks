lst=[]
n=int(input("enter no of elements in list"))
for i in range(1,n+1):
    element=int(input("enter element"))
    lst.append(element)
print(lst) 
new_lst=[]
for j in lst:
    if j not in new_lst:
        new_lst.append(j)
print(new_lst)          

