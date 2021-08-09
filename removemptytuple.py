def emptytuple(l):
    l=[i for i in l if i]
    return l


l= [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(emptytuple(l))