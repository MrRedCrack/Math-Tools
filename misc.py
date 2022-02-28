from decimal import Decimal


def av(*args):
    nums=[Decimal(x) for x in args]
    avg=sum(Decimal(f"{x}") for x in args)/len(args)
    avg=float(avg)
    print(f"{avg = }")

while (inp:=input("Evaluate: ")).upper()!="Q":
    if len(inp)>40:
        break
    eval(inp)