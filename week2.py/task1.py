bimaryNum=input("enter a number")
decimal=0
for i in range(len(bimaryNum)):
    power=len(bimaryNum)-1-i
    decimal+=(int(bimaryNum[i])*(2)**(power))
print(decimal)