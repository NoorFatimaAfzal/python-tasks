def search(lst, n):
    i=0
    found=False
    while i<len(lst):
        if lst[i]==n:
            position=i
            print(f"{n} found at position {position+1}")
            found=True
            break
        i=i+1
    if not found:
        print(f"Not found")
    
lst=[63,3,-82,39]
n=-82

search(lst,n)
    