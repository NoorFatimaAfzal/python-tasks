def gpa():
    noOFsub=int(input("enter number of subjects"))
    sum=0
    numerator=0
    for i in range(1,noOFsub+1):
        ch=int(input(f"enter your credit hours of subject no {i}: "))
        gp=float(input(f"enter your grade points in subject no {i}: "))
        ans=ch*gp
        numerator+=ans
        sum=sum+ch
    gpa=numerator/sum
    if gpa > 3.5:
        print(f"congratulation you have obtained {gpa} gpa !")
    else:
        print(f"you have obtained {gpa} gpa !")
gpa()   
