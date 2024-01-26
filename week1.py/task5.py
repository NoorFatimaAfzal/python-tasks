EQ=input("enter a quadratic equation: ")
positionx2=EQ.find("x^2")
a=EQ[0:positionx2]
positionx11=EQ.find("x")
positionx12=EQ.find("x",positionx11+1)
b=EQ[positionx2+3:positionx12]
c=EQ[positionx12+1:-2]
if a=="-":
    a="-1"
    a=int(a)
elif a=="+":
    a="+1"
    a=int(a)
elif a:
    a=int(a)
else:
    a=1             

if b=="-":
    b="-1"
    b=int(b)
elif b=="+":
    b="+1"
    b=int(b)
elif b:
    b=int(b)
else:
    b=1         

if c=="-":
    c="-1"
    c=int(c)
elif c=="+":
    c="+1"
    c=int(c)
elif c:
    c=int(c)
else:
    c=1
                
print(a)
print(b)
print(c)         
discriment=b**2-4*a*c
if discriment==0:
    print("Roots are real, equal and rational")
elif discriment > 0:
    print("Roots are real, distinct and irrational")  
elif discriment <0:
    print("Roots are imaginary")
else:
    print("not roots")
Xpositive=(-b+(discriment)**(1/2))/(2*a)  
print(Xpositive)
Xnegative=(-b-(discriment)**(1/2))/(2*a)  
print(Xnegative)