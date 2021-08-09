def swap_pos(l,s,d):
    temp=l[s]
    l[s]=l[d]
    l[d]=temp
    return l



l=[23, 65, 19, 90]
pos1 = 1
pos2 = 3
print(swap_pos(l,pos1-1,pos2-1))