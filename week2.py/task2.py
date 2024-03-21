sentence=input("Enter a sentece:")
vowels="aeiouAEIOU"
countV=0
for character in sentence:
    for character1 in vowels:
        if character==character1:
            countV+=1
print(countV)

x=" "
countS=0
for character in sentence:
    for character1 in x:
        if character==character1:
            countS+=1
print(countS)

countC=len(sentence)-(countV+countS)
print(f"no of vowels={countV}")
print(f"no of consonants={countC}")