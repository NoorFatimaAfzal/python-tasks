def factoial(num):
    factoial=1
    if num==1 or num==0:
            return 1
    assert num>0,"Factorial of a negative number is not possible."
    for i in range(1,num+1):
        factoial=factoial*i
    return factoial

no=int(input("enter a number: "))
print(factoial(no))