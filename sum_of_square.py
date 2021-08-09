from typing import TextIO


def sumofsquare(n):
    total=0
    for i in range(1,n+1):
        total=total+(i*i)

    print(total)



sumofsquare(5)