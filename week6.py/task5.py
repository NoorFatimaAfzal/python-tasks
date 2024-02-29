def reverse(string):
    if string=="":
        return""
    else:
        return reverse(string[1:])+string[0]
    
print(reverse("jhsd"))   

#palindrome

def ispalandreom(string):
    if len(string)==0 or len(string)==1:
        return True
    elif string[0]==string[len(string)-1]:
        return ispalandreom(string[1:len(string)-1])
    else:
        return False
    
print(ispalandreom("racecar"))    
        
#decimal to binary
def d_to_b(decimal,result):
    if decimal==0:
        return result
    else:
        result=str(decimal%2)+result
        return d_to_b(decimal//2,result)

print(d_to_b(17,""))            