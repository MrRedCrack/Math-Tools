import traceback
from math import *

def p(lamb,x,mult=False):
    if mult==False:
        print(f"X ~ Po({lamb}) -> P(X = {x})")
        print(f"steps: ({lamb}^{x} * e^-{lamb})/{x}!")
        print('-'*30)
    return (lamb**x*e**(-lamb)/factorial(x))

def pt(lamb,min,max):
    print(f"X ~ Po({lamb}) -> ",end='')
    print(' + '.join([f"P(X = {i})" for i in range(min,max+1)]))
    for i in range(min,max+1):
        if i==min:
            print(f"steps: e^-{lamb} (",end='')
        if i<2:
            if i!=min:
                print(" +",end=' ')
            print(lamb if i!=0 else 1,end='')
        else:
            if i!=min:
                print(" +",end=' ')
            print(f"{lamb}^{i}/{i}!",end='')
        if i==max:
            print(")")
    print('-'*30)
    return sum([p(lamb,i,True) for i in range(min,max+1)])

def bin(n,p,r,disp=True):
    if disp:
        print(f"X ~ B({n}, {p}) -> P(X = {r})")
        print(f"steps: {n}C{r} ({p})^{r} ({1-p:.{len(str(p).split('.')[1])}f})^{n-r}")
        print('-'*30)
    return factorial(n)/(factorial(n-r)*factorial(r))*(p**r)*((1-p)**(n-r))

def binr(n,p,*rs):
    print(f"X ~ B({n}, {p}) -> P(X = {rs[0]})",end='')
    for r in rs[1:]:
        print(f" + P(X = {r})",end='')
    print('')
    print('steps:',' + '.join([f"{n}C{r} ({p})^{r} ({1-p:.{len(str(p).split('.')[1])}f})^{n-r}" for r in rs]))
    print('rslt :',' + '.join(['{:.4g}'.format(bin(n,p,r,False)) for r in rs]))
    print('-'*30)
    return sum([bin(n,p,r,False) for r in rs])

'''
==============================================
print(''+')',
      f"{ = :.4g}\n\n")
==============================================
'''

inp="Evaluate: "
while (opt:=input(inp))!="":
    input("Q-")
    print(f"{'v v v':^{len(opt+inp)}}")
    try:
        string=f"{opt.lower()} = {eval(opt.lower()):.4g}"
        print(f"{string:^{len(opt+inp)}}")
    except:
        if input("error occurred. Display?")!='':
            traceback.print_exc()
    print('\n')



