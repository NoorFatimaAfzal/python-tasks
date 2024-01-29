binaryNum=input("enter a number")
decimal=0
for i in range(len(binaryNum)):
    power=len(binaryNum)-1-i
    decimal+=(int(binaryNum[i])*(2)**(power))
print(decimal)