def chunklist(l,n):
   for i in range(0,len(l),n):
      yield l[i:i+n]
      print(l[i:i+n])


l= ['geeks', 'for', 'geeks', 'like',
    'geeky','nerdy', 'geek', 'love',
    'questions','words', 'life']
n=5
print(list(chunklist(l,n)))