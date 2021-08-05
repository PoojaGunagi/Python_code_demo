def rotate(a,n,d):
    temp=[]
    i=0
    while i<d:
        temp.append(a[i])
        i=i+1
    i=0
    while d<n:
        a[i]=a[d]
        d=d+1
        i=i+1

    a[:]=a[:i]+temp
    return a

l=[1,2,3,4,5,6,7]
print(rotate(l,7,4))
