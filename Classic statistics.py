from math import sqrt
from fractions import Fraction

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
        data=input("Data: ")
        data=[int(i) for i in data.split(" ")]
        data.sort()

        print('')
        datalist=[data[0]]+sum([[' ',x] for x in data[1:]],[])
        blanklist=[' '*len(x) for x in [str(i) for i in datalist]]
        blanklisttop=blanklist.copy()
        # Median
        output=midpoint(data)
        mediantxt,median,indexA,indexB=f"Median, Q2 = {output[0]}",output[1],output[2],output[3]
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
        print('')

        if path[1]=='p': # Population
            print('[Population]')
            # Mean
            mean=round(sum(data)/len(data),4)
            print('Mean >>>')
            print(f"miu = Sigma(x)/N = {sum(data)}/{len(data)} = {mean}")

            # Variance
            var=round(sum([i**2 for i in data])/len(data)-mean**2,4)
            print('\nVariance >>>')
            print(f"sigma^2 = Sigma(x^2)/N - miu^2")
            print(f"        = {sum([i**2 for i in data])}/{len(data)} - {mean**2}")
            print(f"        = {var}")
        
            # Std dev
            print('\nStandard deviation >>>')
            print(f'sigma = sqrt({var}) = {sqrt(var):.4f}')
        
        else: #Sample
            print('[Sample]')
            # Mean
            print('Mean >>>')
            print(f"x-bar = Sigma(x)/n")
            print(f"      = {sum(data)}/{len(data)}")
            print(f"      = {Fraction(sum(data),len(data))}")
            print(f"      = {round(sum(data)/len(data),4)}")
            
            # Variance
            if (p:=int(sum(i**2 for i in data)-(sum(data)**2)/len(data)))%1 == 0:
                var=Fraction(p,(len(data)-1))
                frac=True
            else:
                var=round(p/(len(data)-1),4)
                frac=False
            print('\nVariance >>>')
            print(f"s^2 = (Sigma(x^2) - Sigma(x)^2/n)/(n-1)")
            print(f"    = ({sum(i**2 for i in data)} - ({sum(data)}^2)/{len(data)})/({len(data)}-1)")
            print(f"    = {var}")
            if frac:
                print(f"    = {round(p/(len(data)-1),4)}")
        
            # Std dev
            print('\nStandard deviation >>>')
            print(f's = sqrt({var}) = {sqrt(var):.4f}')

        print('\n')
    elif path[0]=='u':
        pass

    else:
        pass

