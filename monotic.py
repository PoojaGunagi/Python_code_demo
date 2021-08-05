def ismonotic(a):
    flag=0
    for i in range(len(a)-1):
        flag=0
        if (a[i]>=a[i+1]):
            flag=1
    
    if flag==1:
        return True
    else:
        return False


a=[5 ,4 ,4,3,5]
print(ismonotic(a))
               