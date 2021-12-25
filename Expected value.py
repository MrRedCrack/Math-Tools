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
        if '.' in enter1:
            xchk=[len(str(i)[str(i).index('.')+1:]) if i%1!=0 else 0 for i in xs]
            xdecimal=f".{max(xchk)}f"
        else:
            xdecimal=''
        if '.' in str(Pxs[0]):
            pxchk=[len(str(i)[str(i).index('.')+1:]) for i in Pxs]
            pxdecimal=f".{max(pxchk)}f"
        elif '/' in str(Pxs[0]):
            pxdecimal=''
        print(f"x    |"+"|".join([f"{str(i) if '/' in str(i) else i:^7{xdecimal}}" for i in xs]))
        print(f"P(x) |"+"|".join([f"{str(i) if '/' in str(i) else i:^7{pxdecimal}}" for i in Pxs]))
        print('')
        #while (opt:=input("Option: "))!="":
        Ex=sum([num*Pxs[i] for i,num in enumerate(xs)])
        Ex=round(Ex,4) if '.' in str(Ex) else Ex
        Varx=sum([num**2*Pxs[i] for i,num in enumerate(xs)])-Ex**2
        Varx=round(Varx,4) if '.' in str(Varx) else Varx
            #if opt.upper()=="E":
        print(f"E(X) = "+" + ".join([f"{num}({Pxs[i]})" for i,num in enumerate(xs)]))
        print(f"     = {round(Ex,4) if '.' in str(Ex) else str(Ex)}")
        print('')
            #if opt.upper()=="V":
        print(f"Var(X) = E(X^2) - (E(X))^2")
        print(f"       = ("+" + ".join([f"{num}^2 ({Pxs[i]})" for i,num in enumerate(xs)])+f") - {Ex}^2")
        print(f"       = {round(Varx,4) if '.' in str(Varx) else str(Varx)}")
        print('')
            #if opt.upper()=="S":
        print(f"sqrt({Varx}) = {round(sqrt(Varx),4)}")
        print('')
        print('-'*40)

