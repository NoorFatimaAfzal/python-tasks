point1=input("enter point in the form (x1, y1)")
COMMA1at=point1.find(",")
Bracket1of1=point1.find("(")
Bracket2of1=point1.find(")")
x1=point1[Bracket1of1+1:COMMA1at]
print(x1)
y1=point1[COMMA1at+1:Bracket2of1]
print(y1)

point2=input("enter point in the form (x2, y2)")
COMMA2at=point2.find(",")
Bracket1of2=point2.find("(")
Bracket2of2=point2.find(")")
x2=point2[Bracket1of2+1:COMMA2at]
print(x2)
y2=point2[COMMA2at+1:Bracket2of2]
print(y2)

x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)

if x1>0 and y1>0:
    print("point1 lies in 1st quadrant")
elif x1<0 and y1>0:
    print("point1 lies in 2nd quadrant")
elif x1<0 and y1<0:
    print("point1 lies in 3rd quadrant") 
elif x1>0 and y1<0:
    print("point1 lies in 4th quadrant")

if x2>0 and y2>0:
    print("point2 lies in 1st quadrant")
elif x2<0 and y2>0:
    print("point2 lies in 2nd quadrant")
elif x2<0 and y2<0:
    print("point2 lies in 3rd quadrant") 
elif x2>0 and y2<0:
    print("point2 lies in 4th quadrant")

distance= ((x2-x1)**2 + (y2-y1)**2) ** 0.5 
print (f"the distance is {distance}")                 
