def split(l,s):
    temp=[]
    i=0
    while i<s:
        temp.append(l[i])
        i=i+1
    j=0
    while i<len(l):
        l[j]=l[i]
        j=j+1
        i=i+1
    l[:]=l[:j]+temp
    return l





l=[12, 10, 5, 6, 52, 36]
s=2
print(split(l,s))