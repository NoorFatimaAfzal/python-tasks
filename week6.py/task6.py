lst=[1,"noor",[1,2],("noor",),{"noor"}]
new_lst=[]

l=len(lst)
def only(lst,l):
    for i in range(0,l):
        if type(lst[i])!=str:
            return False
        if type(lst[i])==str:
            new_lst.append(lst[i])
            return only(lst,l-1) 
print(only(lst,l))
