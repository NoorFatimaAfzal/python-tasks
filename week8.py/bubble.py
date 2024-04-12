# Write the python program for Bubble Sort algorithm. Also print the list in each
# iteration and total number of swaps which are done for sorting the list.

lst=[3,5,9,-3,78,-238]
swap=0
for i in range(0,len(lst)):
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            temp=lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=temp
            swap+=1
            print(f"Swap no. {swap} : {lst}")
print(f"total no of swaps are {swap}")