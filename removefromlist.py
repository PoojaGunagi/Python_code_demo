def removefromlist(o,r):
    f=[]
    for j in range(len(r)):
        for i in range(len(o)):
            if r[j]==o[i]:
                 o.remove(r[j])

    return o
o=[12, 15, 3, 10]
r=[12, 3]
print(removefromlist(o,r))
