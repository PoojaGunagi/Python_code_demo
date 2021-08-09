def clonecopy(l):
    print("originla list",l)
    c=l[:]
    print("Cloned list",c)
    #using extend
    li_copy = []
    li_copy.extend(l)
    print( li_copy)
    #using list()
    n=list(l)
    print(n)
    li_copy = [i for i in l]
    print(li_copy)
    li=[]
    for item in l: li.append(item)
    print (li)
    li_copy =[]
    li_copy = l.copy()
    print(li_copy)

l=[4, 8, 2, 10, 15, 18]
clonecopy(l)