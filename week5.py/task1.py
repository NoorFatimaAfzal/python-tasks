engineering={"A","B","C","D","E","F"}
no_enggineering={"E","F","G","H"}
both=engineering.intersection(no_enggineering)

print(f"students who applied in both engineering and non engineering are {both}")
all=engineering.union(no_enggineering)
list(all)

print(len(all))