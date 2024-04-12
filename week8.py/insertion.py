lst=[84,-39,83,43,1,0,73,32,9,5]
swap=0
comparisons=0
n=len(lst)
for pass_no in range(1,n):
    i = pass_no
    while i > 0 and lst[i-1] > lst[i]:
        temp=lst[i-1]
        lst[i-1]=lst[i]
        lst[i]=temp
        i-=1
        swap+=1
        comparisons+=1
    print(f"Pass {pass_no}: {lst}")
print(f"Total swaps: {swap}")
print(f"Total comparisons: {comparisons}")
print("======================")

print(lst)