import random
l=[]
def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l

def locate(l,value):
    l = build_random_list(7,7)
    print(l)
    i = 0
    while i < 7:
        if l[i] == value:
            print(i)
        else:
            pass
        i+=1
   

print(build_random_list(7,7))
print(locate(l,1))

##
##     i += 1
##    if value in l:
##        return l.index(value)
##    else:
##        return -1
##def locate(l,value):
##    l = build_random_list(7,7)
##    print(l)
##    i = 0
##    while i < 7 and l[i] != value:
##        i+=1
##    if l[i] == value:
##        return i
##    else:
##        return -1