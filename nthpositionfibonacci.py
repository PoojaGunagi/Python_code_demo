def fibo(k,n):
    n1=0
    n2=1
    total=0
    c=0
    i=2
    while i!=0:
        total=n1+n2
        n1=n2
        n2=total
        if total%k==0:
           c=c+1
           if c==n:
               return i
        i=i+1
    return 
print(fibo(5,4))


