def invert(string,i):
    l=len(string)
    if l>0:
        print(string[l-1],end="")
        invert(string[l-1])
string=input("enter string: ")        
i=len(string)        
invert(string,i)