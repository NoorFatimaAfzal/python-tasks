n1=int(input("enter number of elements in tuple1"))
lst1=[]
for i in range(1,n1+1):
	element=int(input("enter {i} element"))
	lst1.append(element)
tup1=tuple(lst1)

n2=int(input("enter number of elements in tuple1"))
lst2=[]
for i in range(1,n2+1):
	elemnt=int(input("enter {i} element"))
	lst2.append(element)
tup2=tuple(lst2)
ans=[]
for element1 in tup1:
	for element2 in tup2:
		if element1==element2:
			ans.append(element1)
tup3=tuple(ans)
print(tup3)

