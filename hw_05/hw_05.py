l1=[1,4,5,6,8,9,2]

def filterodd(l):
    oddl=[]
    print(l)
    for i in l:
        if i%2 != 0:
            oddl.append(i)
        else:
            pass
    print(oddl)
def mapsquare(l):
    print(l)
    slist=[]
    for i in l:
        slist.append(i**2)
    print(slist)
        
print(filterodd(l1))
print(mapsquare(l1))

            