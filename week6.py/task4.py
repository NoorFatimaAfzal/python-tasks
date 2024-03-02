def power(num,pow):
    if num==0:
        return 0
    elif pow==0:
        return 1
    elif pow==1:
        return num
    else:
        return num*power(num,pow-1)
print(power(2,3))    