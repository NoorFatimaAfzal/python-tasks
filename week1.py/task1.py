#in SI units
bytes=int(input("enter bytes"))
Mbs=bytes/(10**6)
print(f"{bytes} bytes are equal to {Mbs} mega bytes")
Gbs=bytes/(10**9)
print(f"{bytes} bytes are equal to {Gbs} giga bytes")

#in bytes
bytes=int(input("enter bytes"))
Mbs=bytes/(1024**2)
print(f"{bytes} bytes are equal to {Mbs} mega bytes")
Gbs=bytes/(1024**3)
print(f"{bytes} bytes are equal to {Gbs} giga bytes")