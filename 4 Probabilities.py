import traceback
from math import *
from scipy.stats import norm

def p(lamb,x,mult=False):
    if mult==False:
        print(f"X ~ Po({lamb}) -> P(X = {x})")
        print(f"steps: ({lamb}^{x} * e^-{lamb})/{x}!")
        print('-'*30)
    return (lamb**x*e**(-lamb)/factorial(x))

def pt(lamb,min,max):
    print(f"X ~ Po({lamb}) -> ",end='')
    print(' + '.join([f"P(X = {i})" for i in range(min,max+1)]))
    ans=sum([p(lamb,i,True) for i in range(min,max+1)])
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
            print(f")  = {ans:.4f}")
    print('-'*30)
    return ans

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

l,m=0,1
def ni(percent,mode=1,bar=True):
    if not mode:
        print(f"P(Z < {round(norm.ppf(percent),4)}) = {percent}")
    else:
        print(f"P(Z > {round(-norm.ppf(percent),4)}) = {percent}")
    if bar:
        print('-'*30)
    return norm.ppf(percent) if not mode else -norm.ppf(percent)

def nprinter(l,x,u):
    txt='P('
    if l!=None and u==None:
        txt+=f"{x} > {l}"
    elif l!=None:
        txt+=f"{l} < {x}"
    else:
        txt+=x
    if u!=None:
        txt+=f" < {u}"
    txt+=')'
    return txt

def n(mean=0,var=1,l=None,u=None):
    print(f"X ~ N({mean}, {var}) -> {nprinter(l,'X',u)}")
    if isinstance(var,str):
        stddev=sqrt(eval(var))
    else:
        stddev=sqrt(var)
    if l!=None:
        l=round((l-mean)/stddev,2)
        ll=round(norm.cdf(l),4)
        lli=round(1-ll,4)
    if u!=None:
        u=round((u-mean)/stddev,2)
        uu=round(norm.cdf(u),4)
        uui=round(1-uu,4)
    print(f"Converted: {nprinter(l,'Z',u)}")
    if l and u:
        if l<0 and u<0:
            print(f"= P(Z > {abs(u)}) - P(Z > {abs(l)})")
            print(f"= {uu} - {ll} = {uu-ll:.4f} => {round((uu-ll)*100,4)}%")
        elif l<0 and u>0:
            print(f"= 1 - P(Z > {abs(l)}) - P(Z > {u})")
            print(f"= 1 - {ll} - {uui} = {1-ll-uui:.4f} => {round((1-ll-uui)*100,4)}%")
        else:
            print(f"= P(Z > {l}) - P(Z > {u})")
            print(f"= {lli} - {uui} = {lli-uui:.4f} => {round((lli-uui)*100,4)}%")
        ans=norm.cdf(u)-norm.cdf(l)
    elif l!=None:
        if l<0:
            print(f"= 1 - P(Z > {abs(l)})")
            print(f"= 1 - {ll} = {lli} => {round(lli*100,4)}%")
        else:
            print(f"= {lli} => {round(lli*100,4)}%")
        ans=1-norm.cdf(l)
    else:
        if u<=0:
            print(f"= P(Z > {abs(u)})")
            print(f"= {uu:.4f} => {round(uu*100,4)}%")
        else:
            print(f"= 1 - P(Z > {u})")
            print(f"= 1 - {uui} = {1-uui:.4f} => {round((1-uui)*100,4)}%")
        ans=norm.cdf(u)
    print('-'*30)
    return ans

def nr(mean=0,var=1,l=None,u=None):
    return n(mean,var,u=l)+n(mean,var,l=u)

def conf(percent,mean,var):
    if isinstance(var,str):
        stddev=sqrt(eval(var))
    else:
        stddev=sqrt(var)
    if isinstance(mean,str):
        meantrue=round(eval(mean),4)
    else:
        meantrue=mean
    alpha=round((100-percent)/100,4)
    halpha=round(alpha/2,4)
    print(f"alpha = {alpha}")
    print(f"alpha/2 = {halpha}")
    Z=round(ni(halpha,1,False),4)
    val=round(Z*stddev,4)
    print(f"=> Z_{halpha} = {Z}\n")
    print(f"{percent}% CI_miu/p")
    print(f"= {mean} ± {Z} * sqrt({var})")
    print(f"= {meantrue} ± {val}")
    print('-'*30)
    return f"({round(meantrue-val,4)}, {round(meantrue+val,4)})"

def confp(percent,p,size=None):
    if isinstance(p,str):
        ps=[int(A) if float(A)%1==0 else float(A) for A in p.split('/')]
        nume,deno=ps
        insert=p,f"{nume}*{deno-nume}/{deno}**2/{deno}"
    else:
        insert=p,f"{p}*{round(1-p,4)}/{size}"
    return conf(percent,insert[0],insert[1])

def ne(percent,E,stddev):
    alpha=round((100-percent)/100,4)
    halpha=round(alpha/2,4)
    print(f"alpha = {alpha}")
    print(f"alpha/2 = {halpha}")
    Z=round(ni(halpha,1,False),4)
    print(f"=> Z_{halpha} = {Z}\n")
    if isinstance(stddev,str):
        stddevtrue=eval(stddev)
    else:
        stddevtrue=stddev
    print(f"n = ({Z} * {stddev}/{E})^2")
    n=round((Z*stddevtrue/E)**2,4)
    print(f"  = {n} => {ceil(n)}")
    print('-'*30)
    return str(ceil(n))

'''
==============================================
print(''+')',
      f"{ = :.4g}\n\n")
==============================================
'''

inp="Evaluate: "
while (opt:=input(inp))!="" and len(opt)<50:
    input("Q-")
    print(f"{'v v v':^{len(opt+inp)}}")
    try:
        answer=eval(opt.lower())
        if not isinstance(answer,str):
            if str(answer)[str(answer).index('.')+1]!='0' or answer>=1:
                o='.4f'
            else:
                o='.4g'
        else:
            o=0
        string=f"{opt.lower()} = {answer:{o}}"
        print(f"{string:^{len(opt+inp)}}")
    except:
        if input("error occurred. Display?")!='':
            traceback.print_exc()
    print('\n\n')



