def printeven(l):
    for i in range(len(l)):
        if l[i]%2==0:
             print(l[i],end=" ")


l=[2, 7, 5, 64, 14]
printeven(l)
s=4
e=15

# using list comprehension
print( [num for num in l if num % 2 == 0])
print( [num for num in l if num % 2 != 0])

#even number when range is given
print( [num for num in range(s,e+1) if num % 2 == 0])
#odd number when range is given
print( [num for num in range(s,e+1) if num % 2 != 0])