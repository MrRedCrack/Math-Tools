from math import sqrt

while True:
    sample=input("Sample size: ")
    if sample:
        sample=int(sample)
        popmean=(float(A) if float(A)%1!=0 else int(A)) if (A:=input("Population mean, miu: "))!='' else ''
        popvar=input("Population variance, sigma^2: ")
        if popvar:
            popstd=sqrt(float(popvar))
        else:
            popstd=float(input("Population std deviation, sigma: "))
            if popstd%1==0:
                popstd=int(popstd)
        print('')
        if popmean:
            print("Mean of sample means, miu_xbar >>>")
            print(f"= E(Xbar) = {popmean}\n")
        print("Variance of sample means, sigma_xbar^2 >>>")
        if popvar:
            print(f"= Var(Xbar) = {eval(popvar)}/{sample}")
            print(f"            = {round(eval(popvar)/sample,4)}\n")
        else:
            print(f"= Var(Xbar) = {popstd}^2/{sample}")
            print(f"            = {round(popstd**2/sample,4)}\n")
        print("Standard error of the mean, sigma_xbar >>>")
        if popvar:
            print(f"= sqrt({popvar}/{sample})")
            print(f"= {round(sqrt(eval(popvar)/sample),4)}\n")
        else:
            print(f"= {popstd}/sqrt({sample})")
            print(f"= {round(popstd/sqrt(sample),4)}\n")
        print('-'*40)