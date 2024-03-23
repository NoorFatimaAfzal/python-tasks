#name
name = input("Enter your name: ")
try:
    for character in name:
        if character.isdigit():
            raise ValueError
except ValueError:
    print("Sorry! You have typed an invalid name.")
else:
    print("Congratulations! Your name is valid.")

#address
address = input("Enter your address: ")
try:
    if len(address) < 3:
        raise ValueError
except ValueError:
    print("Address cannot be less than 3 characters.")
else:
    print("Congratulations! Your address is valid.")
        
#phone number
phone_num = input("Enter your phone number: ")
try:
    if not phone_num.isdigit() or len(phone_num) != 10:
        raise ValueError
except ValueError:
    print("Sorry! You have typed an invalid number.")
else:
    print("Congratulations! Your number is valid.")

#age
age=int(input("Enter your age : "))
try:
    if age < 0 or age > 150:
        raise ValueError
except ValueError:
    print("Sorry! You have not entered a valid age.")
else:
    print("Congratulations! Your age is valid.")

#gender
gender=input("What is your gender? \n 1. female \n 2. male \n 3. other \n ").capitalize()
try:
    if gender!="Female" or gender!="Male":
        raise Exception
except:
    print ("Gender should be Male or Female ")
else:
    print ("Congratulations ! your gender is successfully added.")


dict={"name": name ,
      "address": address,
      "phone num": phone_num,
      "age": age,
      "gender":gender}
print(dict)