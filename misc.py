from decimal import Decimal


def av(*args):
    avg=sum(Decimal(f"{x}") for x in args)/len(args)
    avg=float(avg)
    print(f"{avg = }")

while (inp:=input("Evaluate: ")).upper()!="Q":
    if len(inp)>50:
        break
    inps=tuple(inp.split(" "))
    a=inps[0]
    print(f"{float(1/Decimal(a)**2)}")
    print()
