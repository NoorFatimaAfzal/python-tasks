phone_book={
    "noor": "03278734825",
    "baba": "0336732788",
    "mama": "0378643769",
    "bhai": "0378468484",
    "aapi": "0378465378"
}
search=input("do you want to search contact number by name ? Y/N").capitalize()
if search=="Y":
    name=input("enter the name of contact: ")
    if name in phone_book:
        print(phone_book[name])

names_display=input("do you want to display the names of all contacts ? Y/N").capitalize()
if names_display=="Y":
    print(phone_book.keys())  

contacts_delete=input("do you want to delete any contact ? Y/N ").capitalize()
if contacts_delete=="Y":
    name="enter the name of contact which you want to delete"
    phone_book.pop(name)           
    print(phone_book)    

contact_update=input("do you want to add a new contact ? Y/N ").capitalize()
if contact_update=="Y":
    new_contact=input("enter name of new contact :")
    contact_number=input(f"Enter contact number of {new_contact} :")
    phone_book.update({new_contact:"037832678"})
    print(phone_book)    

contacts_delete=input("do you want to delete all contacts ? Y/N").capitalize()
if contacts_delete=="Y":
    phone_book.clear()           
    print(phone_book)