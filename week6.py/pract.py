def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]
    
print(reverse("hello"))    