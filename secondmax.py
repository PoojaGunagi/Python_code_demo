def secondmax(l):
    mx=max(l[0],l[1])
    smx=min(l[0],l[1])

    for i in range(2,len(l)):
        if l[i]>mx:
            smx=mx
            mx=l[i]
        elif l[i]>smx and l[i]!=mx:
            smx=l[i]

    return smx

l= [10, 20, 4, 45, 99,99]
print(secondmax(l))
