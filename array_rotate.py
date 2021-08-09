def rotate(l,s,e):
    while s<e:
        temp=l[s]
        l[s]=l[e]
        l[e]=temp
        s=s+1
        e=e-1
    return l






l=[1,2,3,4,5,9,10]
n=len(l)
s=0
e=n-1
print(rotate(l,s,e))
