string=input("enter a string")
upper=lambda string:string.upper()
def reverse(upper=lambda string:string.upper()):
        rev=upper(string)[::-1]
        print(rev)
reverse(upper)        