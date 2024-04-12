lst=[84,-39,83,43,1,0,73,32,9,5]
swap=0
n=len(lst)
for i in range(n-1):
    print(f"Pass {i+1}")
    min=i
    for j in range(i+1,n):
        if lst[j]<lst[min]:
            min=j

    if min != i:
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp
        swap+=1
    print(f"Iteration {i+1}: {lst}")
print(f"Total swaps: {swap}")
print("======================")

print(lst)