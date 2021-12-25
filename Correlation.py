from math import sqrt
from fractions import Fraction

def checkr(r):
    if r<-.75:
        t="Strong negative","-1 < r < -0.75"
    elif r<=-.65:
        t="Moderate negative","-0.75 <= r <= -0.65"
    elif r<0:
        t="Weak negative","-0.65 < r < 0"
    elif r<.65:
        t="Weak positive","0 < r < 0.65"
    elif r<=.75:
        t="Moderate postiive","0.65 <= r <= 0.75"
    elif r<1:
        t="Strong positive","0.75 < r < 1"
    return f"{t[0]} linear relationship: {t[1]}"

while True:
    xs,ys=[],[]
    opt=input("Given: ")
    if not opt or len(opt)>5:
        x=input("xs: ")
        xs=[int(i) if float(i)%1==0 else float(i) for i in x.split(" ")]
        y=input("ys: ")
        ys=[int(i) if float(i)%1==0 else float(i) for i in y.split(" ")]
        print('')
        sumx=sum(xs)
        sumy=sum(ys)
        sumxy=round(sum([round(p*ys[q],4) for q,p in enumerate(xs)]),4)
        sumx2=round(sum([round(p**2,4) for p in xs]),4)
        sumy2=round(sum([round(p**2,4) for p in ys]),4)
        n=len(xs)
        
    else:
        n=int(input("n: "))
        sumx=int(x) if float(x:=input("sum x: "))%1==0 else float(x)
        sumy=int(x) if float(x:=input("sum y: "))%1==0 else float(x)
        sumxy=int(x) if float(x:=input("sum xy: "))%1==0 else float(x)
        sumx2=int(x) if float(x:=input("sum x2: "))%1==0 else float(x)
        sumy2=int(x) if float(x:=input("sum y2: "))%1==0 else float(x)
        print('')
    
    o="^8"
    header=f"{'x':{o}}|{'y':{o}}|{'xy':{o}}|{'x^2':{o}}|{'y^2':{o}}"
    print(header)
    for i,numx in enumerate(xs):
        print(f"{numx:{o}}|{ys[i]:{o}}|{round(numx*ys[i],4):{o}}|{round(numx**2,4):{o}}|{round(ys[i]**2,4):{o}}")
    print('-'*len(header))
    print(f"{sumx:{o}}|{sumy:{o}}|{sumxy:{o}}|{sumx2:{o}}|{sumy2:{o}}")
    print('')

    o=".4f"
    S_XX=round(sumx2-(sumx**2)/n,4)
    S_YY=round(sumy2-(sumy**2)/n,4)
    S_XY=round(sumxy-(sumx*sumy)/n,4)
    print(f"S_XX = {sumx2} - {sumx}^2/{n} = {S_XX}")
    print(f"S_YY = {sumy2} - {sumy}^2/{n} = {S_YY}")
    print(f"S_XY = {sumxy} - {sumx}*{sumy}/{n} = {S_XY}")
    print('')
    
    print("Correlation coefficient >>>")
    r=S_XY/(sqrt(S_XX*S_YY)) # r value
    print(f"r = {S_XY}/(sqrt({S_XX} * {S_YY})) = {r:.4g}")
    print(checkr(r))
    print('')
    print('Coefficient of determination >>>')
    print(f"r^2 = ({r:.4g})^2 = {round(r,4)**2:.4g} -> {round(r,4)**2*100:.2f}% / {100-round(r,4)**2*100:.2f}%")
    print('')
    print('-'*50)

    print("Regression calculation >>>")
    if S_XY%1==0 and S_XX%1==0:
        b=Fraction(int(S_XY),int(S_XX)) 
        print(f"b = S_XY/S_XX = {b} = {round(float(b),4)}")
        print('')
        ym=Fraction(sumy,n)
        xm=Fraction(sumx,n)
        a=ym-b*xm
        print(f"a = Sigma(y)/n - b * Sigma(x)/n")
        print(f"  = {int(sumy)}/{n} - ({b} * {int(sumx)}/{n})")
        print(f"  = {a}")
        if '/' in str(a):
            print(f"  = {round(float(a),4)}")
        print('')
        print(f"regression line: y-cap = {a} + {b}x")
    else:
        b=round(S_XY/S_XX,4)
        print(f"b = S_XY/S_XX = {S_XY}/{S_XX} = {b}")
        print('')
        ym=sumy/n
        xm=sumx/n
        a=round(ym-b*xm,4)
        print(f"a = Sigma(y)/n - b * Sigma(x)/n")
        print(f"  = {int(sumy)}/{n} - ({b} * {int(sumx)}/{n})")
        print(f"  = {a}")
        print('')
        print(f"regression line: y-cap = {a} + {b}x")
    print('')

    if xs:
        if input("Drawing graph? : ")!="":
            print("\nline:")
            print(f"x    |{min(xs):^8}|{max(xs):^8}|")
            print(f"y-cap|{round(a+b*min(xs),2):^8}|{round(a+b*max(xs),2):^8}|")
            print("\ncoordinates:")
            coords=[(x,ys[i]) for i,x in enumerate(xs)]
            coords.sort(key=lambda x:x[0])
            for i,tup in enumerate(coords,1):
                print(f"{i}. {tup}")
        print('')
    print('-'*50)
    while (opt:=input("Predict: "))!='':
        opt=float(opt)
        print(f"y-hat = {a} + {b}({opt}) = {a+b*opt:.4f}")
        print('')
