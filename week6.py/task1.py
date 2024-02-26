def fact(n):
    if n<=1:
        return n
    else:
        return n * fact(n-1)

n=int(input("enter value of n :"))
r=int(input("enter value of r :"))

permutation=fact(n) / fact(n-r)
combination=fact(n) / (fact(r)*fact(n-r))
