def printrepeated(l):
    r=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j] and l[i] not in r:
                r.append(l[i])
    return r


l=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(printrepeated(l))