lowerRange = int(input("Lower value of the range: "))
upperRange = int(input("Upper value of the range: "))
PCount = 0
sum=0
div=2
for num in range(lowerRange,upperRange+1):
    prime = True
    for j in range(2, num):
        if num % j == 0:
            prime = False
            break
    if prime is True:
        print(num)
        sum=sum+num
print(f"sum is {sum}")
