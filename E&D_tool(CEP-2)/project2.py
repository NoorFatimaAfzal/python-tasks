#encryption
key={
    "a":"!",
    "b":"@",
    "c":"#",
    "d":"$",
    "e":"%",
    "f":"^",
    "g":"&",
    "h":"*",
    "i":"(",
    "j":")",
    "k":"_",
    "l":"-",
    "m":"=",
    "n":"+",
    "o":"[",
    "p":"]",
    "q":"{",
    "r":"}",
    "s":"|",
    "t":";",
    "u":":",
    "v":"'",
    "w":'"',
    "x":",",
    "y":"<",
    "z":">",
    " ":"000"
}

sentence=input("Enter a sentence that you want to encrypt: ")
sentence=sentence[::-1]

lst=[]
print("your encrypted sentence is: ",end="")
print("000",end="")
for i in sentence:
    if i in key:
        print(key[i],end="")
        lst.append(key[i])
    else:
        print(i,end="")
        lst.append(i)   
print("000") 
sentence="".join(lst)

#decryption
do=input("Do you want to decrypt the sentence? (yes/no): ")
if do=="yes":
    password=input("Enter the password: ")
    if password=="noor":
        lst=[]
        for i in sentence:
            if i in key.values():
                for j in key:
                    if key[j]==i:
                        lst.append(j)
            else:
                lst.append(i)
        sentence="".join(lst)
        a=list(sentence)
        for i in range(len(a)):
            if a[i] == '0':
                a[i] = ' '
        ulta="".join(a)
        seeda=ulta[::-1]
        print("your decrypted sentence is: ",seeda)
    else:
        print("Thank you for using our encryption service!")
else:
    print("password is incorrect! Thank you for using our encryption service!")