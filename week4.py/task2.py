n=int(input("enternumber of elements of list"))
lst=[]
for i in range(1,n+1):
    element=int(input("enter element"))
    lst.append(element)
lst_with_uniqe_elements=[]
for i in lst:
    if i not in lst_with_uniqe_elements:
        lst_with_uniqe_elements.append(i)
lst_with_uniqe_elements.sort()        
print(lst_with_uniqe_elements[1])            
