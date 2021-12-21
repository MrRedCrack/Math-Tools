from math import sqrt
from fractions import Fraction
from collections import Counter

def midpoint(l,third=False):
    global blanklist
    if len(l)%2==1:
        Qindex=int((len(l)+1)/2)-1
        Qindex2=Qindex*2
        Q=l[Qindex]
        ret=f"{l[Qindex]}",Q,Qindex,Qindex+1
    else:
        QindexB=int(len(l)/2)
        QindexA=QindexB-1
        Qindex2=QindexA*2+1
        Q=(l[QindexA]+l[QindexB])/2
        ret=f"({l[QindexA]}+{l[QindexB]})/2 = {Q}",Q,QindexB,QindexB
    if third:
        Qindex2=-Qindex2-1
    blanklisttop[Qindex2]=blanklisttop[Qindex2].replace(" ",'v')
    blanklist[Qindex2]=blanklist[Qindex2].replace(" ",'^')
    return ret

while True:
    opt=input("[Ungrouped/Grouped] Data: ")
    if opt=='u':
        opt=input("[Population/Sample]: ")
        path=['c',opt]
        print(f"Ungrouped Data ({'Population' if opt=='p' else 'Sample'}).")
    else:
        opt1=input("[Ungrouped/Grouped] Freq dist.: ")
        opt2=input("[Population/Sample]: ")
        path=[opt1,opt2]
        print((f"Grouped Data - {'Ungrouped' if opt1=='u' else 'Grouped'} frequency distribution ({'Population' if opt2=='p' else 'Sample'})."))
    print('')
    if path[0]=='c': # UNGROUPED DATA
        given=input("Given: ")
        if given=='' or len(given)>5:
            data=input("Data: ")
            data=[(int(i) if float(i)%1==0 else float(i)) for i in data.split(" ")]
            dataraw=data.copy()
            data.sort()
            n=len(data)
            sigmax=sum(data)
            sigmax2=sum(i**2 for i in data)

            print('')
            datalist=[data[0]]+sum([[' ',x] for x in data[1:]],[])
            blanklist=[' '*len(x) for x in [str(i) for i in datalist]]
            blanklisttop=blanklist.copy()
            # Median
            output=midpoint(data)
            mediantxt,median,indexA,indexB=f"Q2 = {output[0]} (Median)",output[1],output[2],output[3]
            Q1list=data[:indexA]
            Q3list=data[indexB:]

            # Q1/Q3
            output=midpoint(Q1list)
            Q1txt,Q1=f"Q1 = {output[0]}",output[1]
            output=midpoint(Q3list,True)
            Q3txt,Q3=f"Q3 = {output[0]}",output[1]
            
            print(f"\t{''.join(blanklisttop)}    {Q1txt}")
            print(f"\t{''.join([str(i) for i in datalist])}    {mediantxt}")
            print(f"\t{''.join(blanklist)}    {Q3txt}")
            print(f"{' '*(len(''.join(blanklisttop))+12)}IQR = {Q3}-{Q1} = {Q3-Q1}")
            print(f"{' '*(len(''.join(blanklisttop))+12)}semi-IQR = ({Q3}-{Q1})/2 = {round((Q3-Q1)/2,4)}")
            print(f"{' '*(len(''.join(blanklisttop))+12)}MQR = ({Q3}+{Q1})/2 = {round((Q3+Q1)/2,4)}")
            c=Counter(data)
            mode=[str(k) for k,v in c.items() if v == c.most_common(1)[0][1]]
            print(f"{' '*(len(''.join(blanklisttop))+12)}Mode = {', '.join(mode) if len(mode)!=len(data) else 'no mode'}")
            
            lfence=Q1-1.5*(Q3-Q1)
            lfence=int(lfence) if lfence%1==0 else lfence
            ufence=Q3+1.5*(Q3-Q1)
            ufence=int(ufence) if ufence%1==0 else ufence
            print(f"\nLower fence = {Q1} - 1.5({Q3-Q1}) = {lfence}")
            print(f"Upper fence = {Q3} + 1.5({Q3-Q1}) = {ufence}")
            if any(outliers:=[str(x) for x in data if x<lfence or x>ufence]):
                print(f"Outlier(s): {', '.join(outliers)}")
            print('')

            print(f"n: {n}")
            print(f"Sigma(x): {sigmax}")
            print(f"Sigma(x^2): {sigmax2}")
            print('')

            if input("table? ")!='':
                header=f"{'x':^6}|{'x^2':^8}"
                print('\t'+header)
                for x in dataraw:
                    print(f"\t{x:^6}|{x**2:^8}")
                print('\t'+"-"*len(header))
                print(f"\t{sigmax:^6}|{sigmax2:^8}")
            print('')

        else:
            n=int(input("n: "))
            sigmax=int(input("Sigma(x): "))
            sigmax2=int(input("Sigma(x^2): "))
            print('')

        if path[1]=='p': # Population
            # Mean
            mean=Fraction(sigmax,n) if sigmax%1==0 else sigmax/n
            print('Mean [Population] >>>')
            print(f"miu = Sigma(x)/N")
            print(f"    = {sigmax}/{n}")
            print(f"    = {mean if sigmax%1==0 else round(mean,4)}")
            if '/' in str(mean):
                print(f"    = {round(sigmax/n,4)}")

            # Variance
            mean2=mean**2
            var=Fraction(sigmax2,n)-mean2 if sigmax2%1==0 else round(sigmax2/n-mean2,4)
            print('\nVariance [Population] >>>')
            print(f"sigma^2 = Sigma(x^2)/N - miu^2")
            print(f"        = {sigmax2}/{n} - ({sigmax}/{n})^2")
            print(f"        = {Fraction(sigmax2,n) if sigmax2%1==0 else round(sigmax2/n,4)} - {round(mean2,4)}")
            print(f"        = {var}")
            if '/' in str(var):
                print(f"        = {round(sigmax2/n-mean2,4)}")
        
            # Std dev
            print('\nStandard deviation [Population] >>>')
            print(f'sigma = sqrt({var}) = {sqrt(var):.4f}')
        
        else: #Sample
            # Mean
            print('Mean [Sample] >>>')
            mean=Fraction(sigmax,n) if sigmax%1==0 else round(sigmax/n,4)
            print(f"x-bar = Sigma(x)/n")
            print(f"      = {sigmax}/{n}")
            if str(mean)!=f"{sigmax}/{n}":
                print(f"      = {mean}")
            if '/' in str(mean):
                print(f"      = {round(sigmax/n,4)}")
            
            # Variance
            if (p:=(sigmax2-(sigmax**2)/n))%1 == 0:
                var=Fraction(int(p),(n-1))
                frac=True
            else:
                var=round(p/(n-1),4)
                frac=False
            print('\nVariance [Sample] >>>')
            print(f"s^2 = (Sigma(x^2) - Sigma(x)^2/n)/(n-1)")
            print(f"    = ({sigmax2} - ({sigmax}^2)/{n})/({n}-1)")
            print(f"    = ({sigmax2} - {Fraction(sigmax**2,n) if sigmax2%1==0 else round(sigmax2/n,4)})/{n-1})")
            print(f"    = {var}")
            if frac:
                print(f"    = {round(p/(n-1),4)}")
        
            # Std dev
            print('\nStandard deviation [Sample] >>>')
            print(f's = sqrt({var}) = {sqrt(var):.4f}')

        print('\n')

    elif path[0]=='u': # UNGROUPED FREQUENCY DISTRIBUTION
        pass

    else: # GROUPED FREQUENCY DISTRIBUTION
        pass

