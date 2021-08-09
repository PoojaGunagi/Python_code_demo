def swap(l):
    s=0
    e=len(l)-1
   
    temp=l[s]
    l[s]=l[e]
    l[e]=temp
    return l

l=[12, 35, 9, 56, 24]
l1=[1,2,3]
print(swap(l1))