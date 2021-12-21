from math import sqrt
from fractions import Fraction
import traceback

def fracchk(i):
    return Fraction(int(i.split('/')[0]),int(i.split('/')[1])) if '/' in i and '(' not in i else eval(i)
while True:
    retry=False
    try:
        enter1=input("xs: ")
        enter2=input("Pxs: ")
        xs=[fracchk(i) for i in enter1.split(" ")]
        Pxs=[fracchk(i) for i in enter2.split(" ")]
        Pxtotal=sum(Pxs)

    except:
        retry=True
        traceback.print_exc()
    print('')
    if not retry:
        opt1=input("x has decimal? :")
        if opt1=='f':
            opt1=''
        elif opt1:
            opt1=f".{opt1}f"
        else:
            xs=[int(i) for i in xs]
        opt2=input("P(x) decimal points? :")
        if not opt2:
            opt2=".2f"
        elif opt2=='f':
            opt2=''
        else:
            opt2=f".{opt2}f"
        print('')
        print(f"x    |"+"|".join([f"{str(i) if '/' in str(i) else i:^7{opt1}}" for i in xs]))
        print(f"P(x) |"+"|".join([f"{str(i) if '/' in str(i) else i:^7{opt2}}" for i in Pxs]))
        print('')
        #while (opt:=input("Option: "))!="":
        Ex=sum([num*Pxs[i] for i,num in enumerate(xs)])
        Varx=sum([num**2*Pxs[i] for i,num in enumerate(xs)])-Ex**2
            #if opt.upper()=="E":
        print(f"E(X) = "+" + ".join([f"{num}*{Pxs[i]}" for i,num in enumerate(xs)]))
        print(f"     = {Ex if '/' not in str(Ex) else str(Ex):{'.4f' if '/' not in str(Ex) else 0}}")
        print('')
            #if opt.upper()=="V":
        print(f"Var(X) = E(X^2) - (E(X))^2")
        print(f"       = ("+" + ".join([f"{num}^2*{Pxs[i]}" for i,num in enumerate(xs)])+f") - {Ex}^2")
        print(f"       = {Varx if '/' not in str(Varx) else str(Varx):{'.4f' if '/' not in str(Varx) else 0}}")
        print('')
            #if opt.upper()=="S":
        print(f"sqrt(Var(X)) = {sqrt(Varx):.4f}")
        print('')
    if input("Continue? ").upper()=="N":
        break
