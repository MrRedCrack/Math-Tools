from math import sqrt
from fractions import Fraction
from collections import Counter

def midpoint(l,third=False):
    global blanklist
    if len(l)%2==1:
        Qindex=int((len(l)+1)/2)-1
        Qindex2=Qindex*2
        if third:
            Qindex2=-Qindex2-1
        blanklisttop[Qindex2]=blanklisttop[Qindex2].replace(" ",'v')
        blanklist[Qindex2]=blanklist[Qindex2].replace(" ",'^')
        Q=l[Qindex]
        return f"{l[Qindex]}",Q,Qindex,Qindex+1
    QindexB=int(len(l)/2)
    QindexA=QindexB-1
    Qindex2=QindexA*2+1
    if third:
        Qindex2=-Qindex2-1
    blanklisttop[Qindex2]=blanklisttop[Qindex2].replace(" ",'v')
    blanklist[Qindex2]=blanklist[Qindex2].replace(" ",'^')
    Q=(l[QindexA]+l[QindexB])/2
    return f"({l[QindexA]}+{l[QindexB]})/2 = {Q}",Q,QindexB,QindexB


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
    if path[0]=='c':
        given=input("Given: ")
        if given=='' or len(given)>5:
            data=input("Data: ")
            data=[int(i) for i in data.split(" ")]
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
            print(f"{' '*(len(''.join(blanklisttop))+12)}Mode = {', '.join([str(k) for k,v in c.items() if v == c.most_common(1)[0][1]])}")
            print('')
        else:
            n=int(input("n: "))
            sigmax=int(input("Sigma(x): "))
            sigmax2=int(input("Sigma(x2): "))
            print('')

        if path[1]=='p': # Population
            # Mean
            mean=Fraction(sigmax,n)
            print('Mean >>>')
            print(f"miu = Sigma(x)/N")
            print(f"    = {sigmax}/{n}")
            print(f"    = {mean}")
            if '/' in str(mean):
                print(f"    = {round(sigmax/n,4)}")

            # Variance
            var=Fraction(sigmax2,n)-mean**2
            print('\nVariance >>>')
            print(f"sigma^2 = Sigma(x^2)/N - miu^2")
            print(f"        = {sigmax2}/{n} - ({mean})^2")
            print(f"        = {Fraction(sigmax2,n)} - {mean**2}")
            print(f"        = {var}")
            if '/' in str(var):
                print(f"        = {round(sigmax2/n-mean**2,4)}")
        
            # Std dev
            print('\nStandard deviation >>>')
            print(f'sigma = sqrt({var}) = {sqrt(var):.4f}')
            print('\n--[Population]--')
        
        else: #Sample
            # Mean
            print('Mean >>>')
            mean=Fraction(sigmax,n)
            print(f"x-bar = Sigma(x)/n")
            print(f"      = {sigmax}/{n}")
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
            print('\nVariance >>>')
            print(f"s^2 = (Sigma(x^2) - Sigma(x)^2/n)/(n-1)")
            print(f"    = ({sigmax2} - ({sigmax}^2)/{n})/({n}-1)")
            print(f"    = ({sigmax2} - {Fraction(sigmax**2,n)})/{n-1})")
            print(f"    = {var}")
            if frac:
                print(f"    = {round(p/(n-1),4)}")
        
            # Std dev
            print('\nStandard deviation >>>')
            print(f's = sqrt({var}) = {sqrt(var):.4f}')
            print('\n--[Sample]--')

        print('\n')
    elif path[0]=='u':
        pass

    else:
        pass

