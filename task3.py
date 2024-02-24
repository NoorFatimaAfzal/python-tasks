paragraph=input("enter a paragraph")
lst_of_words=paragraph.split(" ")
print(f"no of words in the given paragraph are : len(lst_of_words)")

new_dict={}
n=1
for word in lst_of_words:
    if word in new_dict:
        new_dict.update({word:n+1})
        
    if word not in new_dict:
        new_dict.update({word:n})
    
print(new_dict)