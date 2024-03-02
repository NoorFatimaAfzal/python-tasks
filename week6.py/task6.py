def only(lst):
    if not lst:
        return []
    if type(lst[0])==str:
        return [lst[0]] + only(lst[1:])
    else:
        return only(lst[1:])
lst = [1, "noor","sjh", [1, 2], ("noor",), {"noor"}, "hjdshj"]
new_lst = only(lst)
print(new_lst)