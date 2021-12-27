from math import sqrt,floor,ceil
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
        Q=round((l[QindexA]+l[QindexB])/2,4)
        ret=f"({l[QindexA]}+{l[QindexB]})/2 = {Q}",Q,QindexB,QindexB
    if third:
        Qindex2=-Qindex2-1
    blanklisttop[Qindex2]=blanklisttop[Qindex2].replace(" ",'v')
    blanklist[Qindex2]=blanklist[Qindex2].replace(" ",'^')
    return ret

def qrt(quartlist,th):
    Ai=floor(th)-1
    Bi=ceil(th)-1
    A=quartlist[Ai]
    B=quartlist[Bi]
    if A==B:
        txt=str(A)
        q=A
    else:
        txt=f"({A}+{B})/2 = {(A+B)/2}"
        q=(A+B)/2
    return txt,q

def grpqrt(qrt):
    qrt=[int(i) for i in qrt.split("/")]
    pos=sumf*qrt[0]/qrt[1]
    pos=pos if pos%1!=0 else int(pos)
    index=0
    while True:
        if pos<=cfs[index]:
            break
        index+=1
    Q=bs[index][0]+(pos-(cfs[index-1] if index!=0 else 0))/fs[index]*(bs[index][1]-bs[index][0])
    Q=round(Q,4) if Q%1!=0 else int(Q)
    Qpostxt=f"{qrt[0]}/{qrt[1]} * {sumf} = {pos}th"
    csize=A if (A:=bs[index][1]-bs[index][0])%1!=0 else int(A)
    Qtxt=f"{bs[index][0]} + ({pos} - {(cfs[index-1] if index!=0 else 0)})/{fs[index]} * {csize}"
    return Qpostxt,Qtxt,Q

while True:
    opt=input("[U]ngrouped/Grouped Data: ")
    if opt=='u':
        opt=input("[P]opulation/Sample: ")
        path=['c',opt]
        print(f"\nUngrouped Data ({'Population' if opt=='p' else 'Sample'}).")
    else:
        opt1=input("[U]ngrouped/Grouped Freq dist.: ")
        opt2=input("[P]opulation/Sample: ")
        path=[opt1,opt2]
        print((f"\nGrouped Data - {'Ungrouped' if opt1=='u' else 'Grouped'} frequency distribution ({'Population' if opt2=='p' else 'Sample'})."))
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
            IQR=round(Q3-Q1,4)
            print(f"{' '*(len(''.join(blanklisttop))+12)}IQR = {Q3}-{Q1} = {IQR}")
            print(f"{' '*(len(''.join(blanklisttop))+12)}semi-IQR = ({Q3}-{Q1})/2 = {round((IQR)/2,4)}")
            print(f"{' '*(len(''.join(blanklisttop))+12)}MQR = ({Q3}+{Q1})/2 = {round((Q3+Q1)/2,4)}")
            c=Counter(data)
            mode=[str(k) for k,v in c.items() if v == c.most_common(1)[0][1]]
            print(f"{' '*(len(''.join(blanklisttop))+12)}Mode = {', '.join(mode) if len(mode)!=len(data) else 'no mode'}")
            
            lfence=Q1-1.5*(IQR)
            lfence=int(lfence) if lfence%1==0 else lfence
            ufence=Q3+1.5*(IQR)
            ufence=int(ufence) if ufence%1==0 else ufence
            print(f"\nLower fence = {Q1} - 1.5({IQR}) = {lfence}")
            print(f"Upper fence = {Q3} + 1.5({IQR}) = {ufence}")
            if any(outliers:=[str(x) for x in data if x<lfence or x>ufence]):
                print(f"Outlier(s): {', '.join(outliers)}")
            Q12=round(median-Q1,4)
            Q23=round(Q3-median,4)
            if Q12>Q23:
                print(f"{Q12} > {Q23}")
                print("=> Q2-Q1 > Q3-Q2 Skewed to the left")
            elif Q12<Q23:
                print(f"{Q12} < {Q23}")
                print("=> Q2-Q1 < Q3-Q2 Skewed to the right")
            else:
                print(f"{Q12} = {Q23}")
                print("=> Q2-Q1 = Q3-Q2 Symmetrical distribution")
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
            print(f'sigma = sqrt({var}) = {round(sqrt(var),4)}')
        
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
            else:
                var=round(p/(n-1),4)
            print('\nVariance [Sample] >>>')
            print(f"s^2 = (Sigma(x^2) - Sigma(x)^2/n)/(n-1)")
            print(f"    = ({sigmax2} - ({sigmax}^2)/{n})/({n}-1)")
            print(f"    = ({sigmax2} - {Fraction(sigmax**2,n) if sigmax2%1==0 else round(sigmax2/n,4)})/{n-1}")
            print(f"    = {var}")
            if '/' in str(var):
                print(f"    = {round(p/(n-1),4)}")
        
            # Std dev
            print('\nStandard deviation [Sample] >>>')
            print(f's = sqrt({var}) = {round(sqrt(var),4)}')

        print('\n')

    elif path[0]=='u': # UNGROUPED FREQUENCY DISTRIBUTION
        given=input("Given: ")
        if given=='' or len(given)>5:
            x=input("xs: ")
            xs=[float(i) if '.' in str(i) else int(i) for i in x.split(" ")]
            f=input("fs: ")
            fs=[int(i) for i in f.split(" ")]
        else:
            data=input("Data: ")
            datas=[float(i) if '.' in str(i) else int(i) for i in data.split(" ")]
            xs,fs=[],[]
            while datas:
                r=datas[0]
                xs.append(r)
                fs.append(datas.count(r))
                datas=[s for s in datas if s!=r]

        sumx=int(p) if (p:=sum(xs))%1==0 else round(p,4)
        sumf=sum(fs)
        sumfx=sum(fs[i]*round(xs[i],4) for i in range(len(xs)))
        sumfx=round(sumfx,4) if sumfx%2!=0 else int(sumfx)
        sumx2=sum(i**2 for i in xs)
        sumx2=round(sumx2,4) if sumx2%1!=0 else int(sumx2)
        sumfx2=round(p,4) if (p:=sum(fs[i]*xs[i]**2 for i in range(len(xs))))%1!=0 else int(p)
        print('')

        o="^8"
        header=f"{'x':{o}}|{'f':{o}}|{'c-f':{o}}|{'fx':{o}}|{'x^2':{o}}"
        print(header)
        cmlf=0
        for i,x in enumerate(xs):
            cmlf+=fs[i]
            fx=int(p) if (p:=x*fs[i])%1==0 else round(p,4)
            x2=int(p) if (p:=x**2)%1==0 else round(p,4)
            print(f"{x:{o}}|{fs[i]:{o}}|{cmlf:{o}}|{fx:{o}}|{x2:{o}}")
        print('-'*len(header))
        print(f"{sumx:{o}}|{sumf:{o}}|{'':{o}}|{sumfx:{o}}|{sumx2:{o}}")
        print('')

        quartlist=sum([[xs[i]]*fs[i] for i in range(len(xs))],[])
        (Q1,q1),(Q2,q2),(Q3,q3)=qrt(quartlist,(sumf+1)/4),qrt(quartlist,(sumf+1)/2),qrt(quartlist,3*(sumf+1)/4)
        print(f"Q1 pos = ({sumf}+1)/4 = {(sumf+1)/4}th")
        print(f" => Q1 = {Q1}")
        print(f"Q2 pos = ({sumf}+1)/2 = {(sumf+1)/2}th")
        print(f" => Q2 = {Q2}")
        print(f"Q3 pos = 3({sumf}+1)/4 = {3*(sumf+1)/4}th")
        print(f" => Q3 = {Q3}")
        lfence=q1-1.5*(IQR)
        lfence=int(lfence) if lfence%1==0 else lfence
        ufence=q3+1.5*(q3-q1)
        ufence=int(ufence) if ufence%1==0 else ufence
        print(f"\nLower fence = {q1} - 1.5({q3-q1}) = {lfence}")
        print(f"Upper fence = {q3} + 1.5({q3-q1}) = {ufence}")
        print('')
        Q12=q2-q1
        Q23=q3-q2
        if Q12>Q23:
            print(f"{Q12} > {Q23}")
            print("Q2-Q1 > Q3-Q2 Skewed to the left")
        elif Q12<Q23:
            print(f"{Q12} < {Q23}")
            print("Q2-Q1 < Q3-Q2 Skewed to the right")
        else:
            print(f"{Q12} = {Q23}")
            print("Q2-Q1 = Q3-Q2 Symmetrical distribution")
        print('')

        if path[1]=='p': # Population
            # Mean
            mean=Fraction(sumfx,sumf) if '.' not in str(sumfx) else round(sumfx/sumf,4)
            print('Mean [Population] >>>')
            print(f"miu = Sigma(fx)/Sigma(f)")
            print(f"    = {sumfx}/{sumf}")
            if str(mean)!=f"{sumfx}/{sumf}":
                print(f"    = {mean}")
            if mean%1!=0:
                print(f"    = {round(sumfx/sumf,4)}")

            # Variance
            mean2=round(p,4) if (p:=mean**2)%1!=0 else int(p)
            var=Fraction(sumfx2,sumf)-mean2 if sumfx2%1==0 else round((sumfx2/sumf)-mean2,4)
            print('\nVariance [Population] >>>')
            print(f"sigma^2 = Sigma(fm^2)/Sigma(f) - miu^2")
            print(f"        = {sumfx2}/{sumf} - ({sumfx}/{sumf})^2")
            print(f"        = {Fraction(sumfx2,sumf) if sumfx2%1==0 else round((sumfx2/sumf),4)} - {mean2}")
            print(f"        = {var}")
            if '/' in str(var):
                print(f"        = {round(float(var),4)}")

            print('\nStandard deviation [Population] >>>')
            print(f"sigma = sqrt({var}) = {round(sqrt(var),4)}")
            print('')
        
        else: # Sample
            # Mean
            mean=Fraction(sumfx,sumf) if '.' not in str(sumfx) else round(sumfx/sumf,4)
            print('Mean [Sample] >>>')
            print(f"x-bar = Sigma(fx)/Sigma(f)")
            print(f"      = {sumfx}/{sumf}")
            if str(mean)!=f"{sumfx}/{sumf}":
                print(f"      = {mean}")
            if mean%1!=0:
                print(f"      = {round(sumfx/sumf,4)}")

            # Variance
            mean2=p if (p:=mean**2)%1!=0 else int(p)
            var=Fraction(p,sumf-1) if (p:=sumfx2-sumf*mean2)%1==0 else round(float(p/(sumf-1)),4)
            print('\nVariance [Sample] >>>')
            print(f"s^2 = (Sigma(fx^2) - Sigma(f) (x-bar^2)) / (Sigma(f)-1)")
            print(f"    = ({sumfx2} - ({sumf}) ({mean})^2) / ({sumf}-1)")
            if (p:=sumfx2-sumf*mean2)%1==0:
                print(f"    = {int(p)}/{sumf-1}")
            print(f"    = {var}")
            if '/' in str(var):
                print(f"    = {round(float(var),4)}")

            print('\nStandard deviation [Sample] >>>')
            print(f"sigma = sqrt({var}) = {round(sqrt(var),4)}")
            print('')

    else: # GROUPED FREQUENCY DISTRIBUTION
        given=input("Given [S]ame/Different class size: ")
        if given=='s':
            c0=input("[lower limit 1] [upper limit 1] [next lower limit]: ")
            cs0=[int(A) if (A:=float(i))%1==0 else A for i in c0.split(" ")]
            f=input("fs: ")
            interval=cs0[2]-cs0[1]
            width=cs0[1]-cs0[0]
            size=width+interval
            hinterval=interval/2

            if f:
                fs=[int(i) for i in f.split(" ")] # Frequencies: fs
            else:
                data=input("Data: ")
                datas=[eval(i) for i in data.split(" ")]
                fs=[0]
                upperbs=[cs0[1]+hinterval]
                for i in datas:
                    index=0
                    while True:
                        chk=upperbs[index]
                        if i<chk:
                            fs[index]+=1
                            break
                        if index+1==len(fs):
                            fs.append(0)
                            upperbs.append(upperbs[index]+size)
                        index+=1
            sumf=sum(fs)

            # Classes: cs
            cs=[[cs0[0],cs0[1]]]
            start=cs0[2]
            for i in range(len(fs)-1):
                cs.append([start,start+width])
                start+=size

            # Boundaries: bs
            bs=[[ A if (A:=x[0]-hinterval)%1!=0 else int(A), B if (B:=x[1]+hinterval)%1!=0 else int(B)] for x in cs]

            # Mid points: ms
            ms=[A if (A:=(x[0]+x[1])/2)%1!=0 else int(A) for x in cs]

            # Cumulative frequencies: cfs
            cf=0
            cfs=[]
            for i in fs:
                cf+=i
                cfs.append(cf)

            # fms
            fms=[A if (A:=round(fs[i]*ms[i],4))%1!=0 else int(A) for i in range(len(fs))]
            sumfms=A if (A:=round(sum(fms),4))%1!=0 else int(A)

            # f(m^2)s
            fm2s=[A if (A:=round(fs[i]*ms[i]**2,4))%1!=0 else int(A) for i in range(len(fs))]
            sumfm2s=A if (A:=round(sum(fm2s),4))%1!=0 else int(A)

            print(f'')
            print(f"{'Class':^7}|{'Boundaries':^12}|{'m':^7}|{'f':^5}|{'Cumulative f':^14}|{'fm':^7}|{'fm^2':^10}Class size = {size}")
            print(f"{'':-^7}+{'':-^12}+{'':-^7}+{'':-^5}+{'':-^14}+{'':-^7}+{'':-^10}")
            for i in range(len(fs)):
                print(f"{'{}-{}'.format(cs[i][0],cs[i][1]):^7}|{'{}-{}'.format(bs[i][0],bs[i][1]):^12}|{ms[i]:^7}|{fs[i]:^5}|{cfs[i]:^14}|{fms[i]:^7}|{fm2s[i]:^10}")
            print(f"{'':-^7}+{'':-^12}+{'':-^7}+{'':-^5}+{'':-^14}+{'':-^7}+{'':-^10}")
            print(f"{'':^7}|{'':^12}|{'':^7}|{sumf:^5}|{'':^14}|{sumfms:^7}|{sumfm2s:^10}")
            print('')

            if input('Drawing histogram/polygon? ')!='':
                print('')
                rfs=[round(i/sumf,4) for i in fs]
                ps=[round(i*100,2) for i in rfs]
                print(f"{'Class':^7}|{'Boundaries':^12}|{'m':^7}|{'f':^5}|{'relative f':^12}|{'percentage':^13}")
                print(f"{'':-^7}+{'':-^12}+{'':-^7}+{'':-^5}+{'':-^12}+{'':-^13}")
                for i in range(len(fs)):
                    print(f"{'{}-{}'.format(cs[i][0],cs[i][1]):^7}|{'{}-{}'.format(bs[i][0],bs[i][1]):^12}|{ms[i]:^7}|{fs[i]:^5}|{rfs[i]:^12}|{ps[i]:^13}")
                print('')
                print(f"Polygon start / end >>> {ms[0]-size} / {ms[-1]+size}")
                print('')
        else:
            c0=input("[ll 1] [ul 1] [ll 2] [ul 2] [ul x].. : ")
            cs0=[int(A) if (A:=float(i))%1==0 else A for i in c0.split(" ")]
            f=input("fs: ")
            interval=cs0[2]-cs0[1]
            hinterval=interval/2

            # Classes
            cs=[[cs0[0],cs0[1]],[cs0[2],cs0[3]]]
            lltemp=cs0[3]
            for x in cs0[4:]:
                lltemp+=interval
                if lltemp%1==0:
                    lltemp=int(lltemp)
                cs.append([lltemp,x])
                lltemp=x
            
            # Boundaries
            bs=[[A if (A:=x[0]-hinterval)%1!=0 else int(A),B if (B:=x[1]+hinterval)%1!=0 else B] for x in cs]
            
            # Class sizes
            Cs=[A if (A:=x[1]-x[0])%1!=0 else int(A) for x in bs]
            
            if f:
                fs=[int(i) for i in f.split(" ")]
            else:
                data=input("Data: ")
                datas=[eval(i) for i in data.split(" ")]
                fs=[0]*len(cs)
                for i in datas:
                    upperb=cs[0][1]+hinterval
                    index=0
                    while True:
                        if i<upperb:
                            fs[index]+=1
                            break
                        upperb+=Cs[index+1]
                        index+=1
            sumf=sum(fs)

            # Mid points
            ms=[A if (A:=sum(x)/2)%1!=0 else int(A) for x in cs]

            # Cumulative frequencies: cfs
            cf=0
            cfs=[]
            for i in fs:
                cf+=i
                cfs.append(cf)

            # Frequency densities: fds
            fds=[A if (A:=round(fs[i]/Cs[i],4))%1!=0 else int(A) for i in range(len(fs))]

            # fms
            fms=[A if (A:=round(fs[i]*ms[i],4))%1!=0 else int(A) for i in range(len(fs))]
            sumfms=A if (A:=round(sum(fms),4))%1!=0 else int(A)

            # f(m^2)s
            fm2s=[A if (A:=round(fs[i]*ms[i]**2,4))%1!=0 else int(A) for i in range(len(fs))]
            sumfm2s=A if (A:=round(sum(fm2s),4))%1!=0 else int(A)

            print(f'')
            print(f"{'Class':^7}|{'Boundaries':^12}|{'c':^5}|{'m':^7}|{'f':^5}|{'Cumulative f':^14}|{'fm':^7}|{'fm^2':^10}")
            print(f"{'':-^7}+{'':-^12}+{'':-^5}+{'':-^7}+{'':-^5}+{'':-^14}+{'':-^7}+{'':-^10}")
            for i in range(len(fs)):
                print(f"{'{}-{}'.format(cs[i][0],cs[i][1]):^7}|{'{}-{}'.format(bs[i][0],bs[i][1]):^12}|{Cs[i]:^5}|{ms[i]:^7}|{fs[i]:^5}|{cfs[i]:^14}|{fms[i]:^7}|{fm2s[i]:^10}")
            print(f"{'':-^7}+{'':-^12}+{'':-^5}+{'':-^7}+{'':-^5}+{'':-^14}+{'':-^7}+{'':-^10}")
            print(f"{'':^7}|{'':^12}|{'':^5}|{'':^7}|{sumf:^5}|{'':^14}|{sumfms:^7}|{sumfm2s:^10}")
            print('')

            if input('Drawing histogram? ')!='':
                print('')
                rfs=[round(i/sumf,4) for i in fs]
                ps=[round(i*100,2) for i in rfs]
                print(f"{'Class':^7}|{'Boundaries':^12}|{'c':^7}|{'f':^5}|{'f density':^12}")
                print(f"{'':-^7}+{'':-^12}+{'':-^7}+{'':-^5}+{'':-^12}")
                for i in range(len(fs)):
                    print(f"{'{}-{}'.format(cs[i][0],cs[i][1]):^7}|{'{}-{}'.format(bs[i][0],bs[i][1]):^12}|{Cs[i]:^7}|{fs[i]:^5}|{fds[i]:^12}")
                print('')

        if input("Drawing ogive? ")!='':
            print('')
            crfs=[round(A,4) if (A:=i/sumf)%1!=0 else int(A) for i in cfs]
            cps=[round(A,4) if (A:=i*100)%1!=0 else int(A) for i in crfs]
            pc=[f"<{cs[0][0]-interval}",f"<{bs[0][0]}",0,0,0]
            print(f"{'Upper':^10}|{'Cumulative':^12}|{'Cumulative':^12}|{'Cumulative':^13}")
            print(f"{'Boundaries':^10}|{'frequency':^12}|{'relative f':^12}|{'percentage':^13}")
            print(f"{'':-^10}+{'':-^12}+{'':-^12}+{'':-^13}")
            print(f"{pc[1]:^10}|{pc[2]:^12}|{pc[3]:^12}|{pc[4]:^13}")
            for i in range(len(cfs)):
                print(f"{'{}{}'.format('<',bs[i][1]):^10}|{cfs[i]:^12}|{crfs[i]:^12}|{cps[i]:^13}")
        print('')

        Q1pos,Q1txt,Q1=grpqrt('1/4')
        print(f"Q1 pos = {Q1pos}")
        print(f"Q1 = {Q1txt}")
        print(f"   = {Q1}\n")
        Q2pos,Q2txt,Q2=grpqrt('1/2')
        print(f"Q2 pos = {Q2pos}")
        print(f"Q2 = {Q2txt}")
        print(f"   = {Q2} (Median)\n")
        Q3pos,Q3txt,Q3=grpqrt('3/4')
        print(f"Q3 pos = {Q3pos}")
        print(f"Q3 = {Q3txt}")
        print(f"   = {Q3}\n")
        print(f"IQR = {Q3} - {Q1} = {round(Q3-Q1,4)}\n")
        while (predict:=input("Predict percent? "))!='':
            xpos,Qxtxt,Qx=grpqrt(predict)
            print(f"x pos = {xpos}")
            print(f"x = {Qxtxt}")
            print(f"  = {Qx}")
            print('')
        print('')

        # Mode
        if given=='s':
            modeindex=fs.index(max(fs))
            Lm=bs[modeindex][0]
            f_m=fs[modeindex]
            f_b=0 if modeindex==0 else fs[modeindex-1]
            f_a=0 if modeindex+1==len(fs) else fs[modeindex+1]
            mode=round(Lm+(f_m-f_b)/(2*f_m-f_a-f_b)*size,4)
            print("Mode [Equal class width] >>>")
            print(f"Modal class = \"{cs[modeindex][0]}-{cs[modeindex][1]}\"")
            print(f"M = {bs[modeindex][0]} + ({f_m}-{f_b})/(({f_m}-{f_b})+({f_m}-{f_a})) * {size}")
            print(f"  = {mode}")
        else:
            modeindex=fds.index(max(fds))
            Lm=bs[modeindex][0]
            p_m=fds[modeindex]
            p_b=0 if modeindex==0 else fds[modeindex-1]
            p_a=0 if modeindex+1==len(fs) else fds[modeindex+1]
            C=A if (A:=bs[modeindex][1]-bs[modeindex][0])%1!=0 else int(A)
            mode=round(Lm+(p_m-p_b)/(2*p_m-p_a-p_b)*C,4)
            print("Mode [Unequal class width] >>>")
            print(f"Modal class = \"{cs[modeindex][0]}-{cs[modeindex][1]}\"")
            print(f"M = {bs[modeindex][0]} + ({p_m}-{p_b})/(({p_m}-{p_b})+({p_m}-{p_a})) * {C}")
            print(f"  = {mode}")
        print('')

        print('-'*50)
        if path[1]=='p':
            # Mean
            mean=round(sumfms/sumf,4)
            print(f"Mean [Population] >>>")
            print(f"miu = Sigma(fm)/Sigma(f)")
            print(f"    = {sumfms}/{sumf}")
            print(f"    = {mean}")

            # Variance
            mean2=(sumfms/sumf)**2
            var=round(sumfm2s/sumf-mean2,4)
            print(f"\nVariance [Population] >>>")
            print(f"sigma^2 = Sigma(fm^2)/Sigma(f) - miu^2")
            print(f"        = {sumfm2s}/{sumf} - ({sumfms}/{sumf})^2")
            print(f"        = {var}")

            # Std dev
            print(f"\nStandard deviation [Population] >>>")
            print(f"sigma = sqrt({var}) = {round(sqrt(var),4)}")
        else:
            # Mean
            mean=round(sumfms/sumf,4)
            print(f"Mean [Sample] >>>")
            print(f"x-bar = Sigma(fm)/Sigma(f)")
            print(f"      = {sumfms}/{sumf}")
            print(f"      = {mean}")

            # Variance
            var=round((sumfm2s-(sumfms**2)/sumf)/(sumf-1),4)
            print(f"\nVariance [Sample] >>>")
            print(f"s^2 = (Sigma(fm^2) - Sigma(fm)^2/Sigma(f)) / Sigma(f) - 1")
            print(f"    = ({sumfm2s}-{sumfms}^2/{sumf})/{sumf} - ({sumf}-1)")
            print(f"    = {var}")

            # Std dev
            print(f"\nStandard deviation [Sample] >>>")
            print(f"sigma = sqrt({var}) = {round(sqrt(var),4)}")
        print('')
        print(f"mean, median, mode = {mean}, {Q2}, {mode}")
        if mean>Q2>mode:
            print(f"mean > median > mode")
            print(f"{mean} > {Q2} > {mode}")
            print('skewed to the right (mean most right)')
        elif mean<Q2<mode:
            print(f"mean < median < mode")
            print(f"{mean} < {Q2} < {mode}")
            print('skewed to the left (mean most left)')
        print('')
