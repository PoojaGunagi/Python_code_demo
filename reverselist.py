def reverselist(l):
      l.reverse()
      return l

def reverselist1(l):
      new_l=l[::-1]
      return new_l


list = [10, 11, 12, 13, 14, 15]
print(reverselist1(list))
print(reverselist(list))
