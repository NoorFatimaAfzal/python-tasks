num=input("enter a number: ")
numREVERSE=num[::-1]
if num==numREVERSE:
    print("yes! it is a  palindrome ")
else:
    print("No! it is not a palindrome ")   

#with recursion

def ispalindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return ispalindrome(string[1:-1])

string = input("Enter a string: ")
print(ispalindrome(string))      