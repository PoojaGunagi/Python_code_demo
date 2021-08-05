from typing import TextIO


def remainder(l,n):
    total=1
    for i in range(0,len(l)):
        total=total*l[i]

    rem=total%n
    return rem


l=[100, 10, 5, 25, 35, 14]
n=11
print(remainder(l,n))