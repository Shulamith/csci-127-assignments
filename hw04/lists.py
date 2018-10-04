import random
l=[]
l2 = [2,4,5,4]
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
    l = build_random_list(7,7) #maybe I don't want to do this, maybe I just want a regular list? Like form one beforehand? or do i want to build one each time?outside function?
    print(l)
    i = 0
    while i < 7: #7 only makes sense now--beware!
        if l[i] == value:
            print(i) #I can use return instead if I only want to look for it once. If I want to print it each time I have to figure out how to do the -1 when there is nothing ever.
        else:
            pass
        i+=1
def count(l2,value2):
    print("l2",l2)
    i = 0
    appears_list = 0
    while i < len(l2):
        if l2[i] == value2:
            appears_list +=1
        else:
            pass
        i+=1
    return appears_list
            

print(build_random_list(7,7))
print(locate(l,1))
print(count(l2,4))

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
