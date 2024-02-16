def tuple_intersection(tup1,tup2):
	ans=[]
	for element1 in tup1:
		for element2 in tup2:
			if element1==element2 and element1 not in ans:
				ans.append(element1)
	tup3=tuple(ans)
	return tup3

#input first list
n1=int(input("enter number of elements in tuple 1:"))
lst1=[]
for i in range(1,n1+1):
	element1=int(input(f"enter {i} element"))
	lst1.append(element1)
tup1=tuple(lst1)
#input 2nd list
n2=int(input("enter number of elements in tuple 2:"))
lst2=[]
for i in range(1,n2+1):
	element2=int(input(f"enter {i} element"))
	lst2.append(element2)
tup2=tuple(lst2)
#call function
print(tuple_intersection(tup1,tup2))

