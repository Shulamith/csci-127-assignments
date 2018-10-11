l1=[1,4,5,6,8,9,2]

    
##def filterodd(l):
##    oddl=[]
##    for i in l:
##        if l[i] % 2 != 0:
##            oddl.append(l[i])
##        else:
##            pass
    
        
##print(filterodd(l1))
            
##def filterodd(l):
##    oddl=[]
##    i=0
##    print(l)
##    while i < len(l):
##        if l[i]%2 != 0:
##            oddl.append(l[i])
##            i+=1
##        else:
##            i+=1
##    print(oddl)
##    
##        
##print(filterodd(l1))
##
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

            