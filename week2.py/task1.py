binaryNum=input("enter a number")
decimal=0
for i in range(len(binaryNum)):
    power=len(binaryNum)-1-i
    decimal+=(int(binaryNum[i])*(2)**(power))
print(decimal)

#with recursion

def binaryToDecimal(binaryNum):
    if len(binaryNum)==0:
        return 0
    else:
        return (int(binaryNum[0])*(2)**(len(binaryNum)-1))+binaryToDecimal(binaryNum[1:])
    
#decimal to binary 
#with recursion   
    
def decimalToBinary(decimal):
    if decimal==0:
        return ""
    else:
        return decimalToBinary(decimal//2)+str(decimal%2)    