a=int(input("enter first number"))
b=int(input("enter 2nd number"))
larger= lambda a,b:max(a,b)

def table (larger=lambda a,b:max(a,b)):
    extent=int(input("enter upto what extent"))
    for i in range(1,extent+1):
        product=larger(a,b)*i
        print (f"{larger(a,b)}*{i}={product}")
table(larger)        


