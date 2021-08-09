def check(a):
    if a<0:
        print("invalid input")
    elif(a==1):
        print("neither prime nor non-prime")
    else:
        for i in range(2,a):
            flag=0
            if a%i==0:
                print(a,"is not prime number")
                break
            else:
                flag=1
        if flag==1:
            print(a, " is prime number")


check(11)