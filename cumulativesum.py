def cumulativesum(l):
    sum=0
    r=[]
    for i in range(len(l)):
        sum=sum+l[i]
        r.append(sum)
    
    return r



l=[10, 20, 30, 40, 50]
print(cumulativesum(l))