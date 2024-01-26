ECATmarks=int(input("enter your ECAT marks:"))
ECATaggregate=(ECATmarks/400)*33

obtainedINTERmarks=int(input("enter your obtained INTER part 1 marks:"))
totalINTERmarks=int(input("enter your total INTER part 1 marks:"))
INTERaggregate=(obtainedINTERmarks/totalINTERmarks)*50

MATRICmarks=int(input("enter your MATRIC marks:"))
MATRICaggregate=(MATRICmarks/1100)*17

totalAGG=ECATaggregate+INTERaggregate+MATRICaggregate
print(totalAGG)