
def getorder(n):
    o=0
    while(n!=0):
        o=o+1
        n=n//10
    return o

def armstrong(n):
    total=0
    p=getorder(n)
    t=n
    while(n>0):
        temp=(n%10)
        total=total+pow(temp,p)
        n=n//10

    if total==t:
        print(t," is armstrong number")
    else:
        print(t, "is not armstrong number")

armstrong(151)
armstrong(1634)


