from math import sqrt
from fractions import Fraction

def checkr(r):
    if r<-.75:
        return "Strong negative correlation: -1 < r < -0.75"
    elif r<=-.65:
        return "Moderate negative correlation: -0.75 <= r <= -0.65"
    elif r<0:
        return "Weak negative correlation: -0.65 < r < 0"
    elif r<.65:
        return "Weak positive correlation: 0 < r < 0.65"
    elif r<=.75:
        return "Moderate postiive correlation: 0.65 <= r <= 0.75"
    elif r<1:
        return "Strong positive correlation: 0.75 < r < 1"

while True:
    xs,ys=[],[]
    opt=input("Given: ")
    if not opt:
        x=input("xs: ")
        xs=[int(i) for i in x.split(" ")]
        y=input("ys: ")
        ys=[int(i) for i in y.split(" ")]
        print('')
        sumx=sum(xs)
        sumy=sum(ys)
        sumxy=sum([p*ys[q] for q,p in enumerate(xs)])
        sumx2=sum([p**2 for p in xs])
        sumy2=sum([p**2 for p in ys])
        n=len(xs)
        
    elif opt:
        n=int(input("n: "))
        sumx=int(input("sum x: "))
        sumy=int(input("sum y: "))
        sumxy=int(input("sum xy: "))
        sumx2=int(input("sum x2: "))
        sumy2=int(input("sum y2: "))
    
    o="^5"
    header=f"{'x':{o}}|{'y':{o}}|{'xy':{o}}|{'x^2':{o}}|{'y^2':{o}}"
    print(header)
    for i,numx in enumerate(xs):
        print(f"{numx:{o}}|{ys[i]:{o}}|{numx*ys[i]:{o}}|{numx**2:{o}}|{ys[i]**2:{o}}")
    print('-'*len(header))
    print(f"{sumx:{o}}|{sumy:{o}}|{sumxy:{o}}|{sumx2:{o}}|{sumy2:{o}}")
    print('')

    if input("Drawing graph? : ")!="":
        coords=[(x,ys[i]) for i,x in enumerate(xs)]
        coords.sort(key=lambda x:x[0])
        for i,tup in enumerate(coords,1):
            print(f"{i}. {tup}")
    print('')
    
    o=".4f"
    S_XX=round(sumx2-(sumx**2)/n,6)
    S_YY=round(sumy2-(sumy**2)/n,6)
    S_XY=round(sumxy-(sumx*sumy)/n,6)
    print(f"S_XX = {sumx2} - {sumx}^2/{n} = {S_XX:{o}}")
    print(f"S_YY = {sumy2} - {sumy}^2/{n} = {S_YY:{o}}")
    print(f"S_XY = {sumxy} - {sumx}*{sumy}/{n} = {S_XY:{o}}")
    print('')
    
    print("Correlation coefficient:")
    r=S_XY/(sqrt(S_XX)*sqrt(S_YY)) # r value
    print(f"r = {S_XY:{o}}/(sqrt({S_XX:{o}})*sqrt({S_YY:{o}})) = {r:.4g}")
    print(checkr(r))
    print('')
    print('Coefficient of determination:')
    print(f"r^2 = ({r:.4g})^2 = {round(r,4)**2:.4g} -> {round(r,4)**2*100:.2f}% / {100-round(r,4)**2*100:.2f}%")
    print('')
    print('-'*50)

    print("Regression calculation:")
    if S_XY%1==0 and S_XX%1==0:
        b=Fraction(int(S_XY),int(S_XX)) 
        print(f"b = S_XY/S_XX = {b}")
        ym=Fraction(sumy,n)
        xm=Fraction(sumx,n)
        a=ym-b*xm
        print(f"a = Sigma(y)/n - b * Sigma(x)/n")
        print(f"  = {int(sumy)}/{n} - ({b} * {int(sumx)}/{n})")
        print(f"  = {a}")
        print('')
        print(f"regression line: y-cap = {a} + {b}x")
    else:
        b=round(round(S_XY,4)/round(S_XX,4),4)
        print(f"b = S_XY/S_XX = {S_XY:.4f}/{S_XX:.4f} = {b:.4f}")
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
    print('-'*50)
    while (opt:=input("Predict: "))!='':
        opt=float(opt)
        print(f"y-hat = {a} + {b}({opt}) = {a+b*opt:.4f}")
        print('')
