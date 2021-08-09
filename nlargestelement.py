def nlarge(l,n):
    l.sort()
    return l[-n:]


l=[81, 52, 45, 10, 3, 2, 96]
n=3
print(nlarge(l,n))
