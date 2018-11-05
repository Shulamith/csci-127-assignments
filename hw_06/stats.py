#value between 0 to 10 (including and excluding doesn't matter"
#Kushendra Ramrup and Shulamit
import random
l=[]
def build_random_list(size,max_value):
    l = [] # start with an empty list
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
def max_index(l):
    i=0
    for x in range(1,len(l)):
        if l[x]>l[i]:
            i = x
    return i
##
##    while i<len(l):
##        if l[i] == max:
##            return i
##        else:
##            i+=1
##print(build_random_list(100,11))


##def max(l):
##    i=0
##    for x in range(0,len(l)):
##        if l[x]>l[i]:
##            i = x
##    return l[i]

def freq(l,val):
    count = 0 
    for item in l:
        if item == val:
            count+=1
        else:
            pass
    return count
l1= build_random_list(4,30)
l2=build_random_list(100,11)
#print(l1)
print(l2,"the index of the max is:",max_index(l2))
print("The freq of 7 is",freq(l2,7))

##print(max(l2))

def mode(l):
    possible_mode = []
    frequency=[]
    mode = []
    i=1
    for item in l:
        count = freq(l,item)
        if count >= i:
            i=count
            if item>=2 and item not in possible_mode:
                possible_mode.append(item)
                frequency.append(count)
                
    if i == 1:
        return ("They all appear one time",l)
    
    
##        frequency.append(count)
##   print(frequency)
##    mode = max(frequency)
    else:      
        mostfrequent=max_index(frequency)
        mode = possible_mode[mostfrequent] 
        return mode
        
        
print("The mode is:",mode(l2))    
        
        
        