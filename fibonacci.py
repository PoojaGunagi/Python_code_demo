
def fibonacci(n):
    n1=0
    n2=1
    total=0
    if n<0:
        return "invalid input"
    elif n==0:
        return n1
    elif n==1:
        return n2
    else:
        print(n1,n2,end=" ")
        for i in range(2,n+1):
            total=n1+n2
            print(total,end=" ")
            n1=n2
            n2=total


def recusivefibo(n):
    #git initprint(n)
    if n<=0:
        return "invalid"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return recusivefibo(n-1)+recusivefibo(n-2)

recusivefibo(30)

fibonacci(30)