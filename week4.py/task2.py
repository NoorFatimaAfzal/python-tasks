n=int(input("enter number of elements of list"))
lst=[]
for i in range(1,n+1):
    element=int(input("enter element"))
    lst.append(element)
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
new_lst.sort()        
print(new_lst[1])            
