lst = [1, "noor", [1, 2], ("noor",), {"noor"}, "hjdshj"]
new_lst = []

def only(lst):
    for i in lst[:]:
        if type(i)==type("jhs"): 
            lst.remove(i) 
            new_lst.append(i)
    return new_lst
print(only(lst))
