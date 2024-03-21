# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()   
# for k in range(n-1,0,-1):
#     for l in range(k,0,-1):
#             print("*",end="")
#     print()  
#with recursion
def star(n):
    if n==0:
        return
    else:
        star(n-1)
        print("*"*n)
         
star(4)     