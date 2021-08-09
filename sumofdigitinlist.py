def sumofdigitinlist(l):
    r=[]
    sum=0
    for i in range(len(l)):
        sum=0
        while(l[i]!=0):
            temp=l[i]%10
            sum=sum+int(temp)
            l[i]=l[i]/10
        r.append(sum)
    return r

l=[12, 67, 98, 34]
print(sumofdigitinlist(l))