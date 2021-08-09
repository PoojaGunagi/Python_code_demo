def large():
    n=4
    l=[9,67,8,100]
    m=0
    for i in range(0,n):
        if l[i]>m:
            m=l[i]

    print(m)

large()