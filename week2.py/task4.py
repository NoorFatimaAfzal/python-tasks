import random
upto=int(input("enter a number"))
Capitals=input("do you want to have capital charactrs ? y/n")
Small=input("do you want to have small charactrs ? y/n")
special=input("do you want to have special charactrs ? y/n")
n=input("do you want to have numbers ? y/n")
em=input("do you want to have emogies ? y/n")

ToInclude=""
if Capitals=="y" or Capitals=="Y":
    ToInclude+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if Small=="y" or Small=="Y":
    ToInclude+="abcdefijklmnopqrstuvwxyz"
if special=="y" or special=="Y":
    ToInclude+="!@#$%^&*()\'\"}{[]_-+=?><:"  
if n=="y" or n=="Y":
    ToInclude+="1234567890" 
if em=="y" or em=="Y":
    ToInclude+="😀😃👑😄🎓😁😆👒🧢😅😂🎩🤣"
for password in range(upto):
    password="".join(random.choice(ToInclude))    
    print(password,end="")           

