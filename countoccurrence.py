def countoccurrence(l,f):
    c=0
    for i in range(len(l)):
        if l[i]==f:
            c=c+1
    return c


l=[15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(countoccurrence(l,x))
print(l.count(x))