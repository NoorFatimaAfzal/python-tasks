f=int(input("enter temp in fahrenheit"))
def fTOc (fah):
    
    c=5/9*(f-32)
    return c
c=int(input("enter temp in celcius"))
def cTOf (cel):
    
    f=c*(9/5)+32
    return f

print(f"{c} in fahrenheit is {cTOf(c)}")
print(f"{c} in celcius is {fTOc(c)}")