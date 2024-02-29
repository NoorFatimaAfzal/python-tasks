import random
lst=[]
for i in range(0,11):
    a=random.randint(0,1000)
    lst.append(a)
print(lst)    

l=len(lst)
def sum_lst(lst,l):
    if lst[len(lst)-1]==0:
        return 
    else:
        return lst[l-1]+sum_lst(lst,l-1)
    
print(sum(lst))    