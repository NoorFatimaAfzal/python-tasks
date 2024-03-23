def DecimalToBinary(num):
    try:
        print(f"The hexadecimal value of {num} is %x." %num)
    except: 
        num=int(num)
        print(f"The hexadecimal value of {num} is %x." %num)
    else:    
        print("function called succesfully")

num=input("Enter a number: ")
DecimalToBinary(num)
