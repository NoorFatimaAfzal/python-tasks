n=int(input("enter value of n"))
r=int(input("enter value of r"))
def per (n,r):
    nfact=1
    rfact=1
    NRfact=1
    for i in range(1,n+1):
        nfact=nfact*i
    for k in range(1,n-r+1):
        NRfact=NRfact*k 
    permutation=nfact/NRfact
    return permutation
print(per(n,r))

def comb (n,r):
    nfact=1
    rfact=1
    NRfact=1
    for i in range(1,n+1):
        nfact=nfact*i
    for j in range(1,r+1):
        rfact=rfact*j
    for k in range(1,n-r+1):
        NRfact=NRfact*k 
    permutation=nfact/(rfact*NRfact)
    return permutation
print(comb(n,r))






