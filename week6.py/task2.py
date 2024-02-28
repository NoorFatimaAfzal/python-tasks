def fab(n):
    if n <= 1:
        return n
    return fab(n-1) + fab(n-2)
n=5
if n<=0:
    print("Incorrect input")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fab(i))


                      