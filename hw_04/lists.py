import random
l=[]
l2 = [2,4,5,4]
l3=[1,6,9,10]
l4=[5,6,7,8,8,7,6,5]
l5=[8,3,5,3,8]
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
def locate(l,value): #looks for the first time the value is in the list and prints that postion
    print(l,"Searching for:",value)
    i = 0
    while i <len(l): 
        if l[i] == value:
            return(i) #because this is return, it will only return first time the value is in the list
        else:
            i+=1
    return -1
def count(l,value2):
    print(l,"Counting:",value2)
    i = 0
    appears_list = 0
    while i < len(l):
        if l[i] == value2:
            appears_list +=1
        else:
            pass
        i+=1
    return appears_list
def reverse(l):
    print(l)
    rlist=[]
    i=1
    while i<=len(l):
        rlist.append(l[len(l)-i])
        i+=1
    return rlist
def isIncreasing(l):
    print("Is this list increasing:",l)
    i=0
    while i<=len(l):
        if l[i+1] > l[i]:
            i+=1
        else:
            return False
        return True
def palindrome(l):
    print("is this a palindrome:",l)
    i=0
    leng = len(l)
    while i<=(leng/2):
        if l[i] == l[(leng-(i+1))]:
            i+=1
        else:
            return False
        return True
l1 = build_random_list(6,7)
l2 = build_random_list(10,8)
print(l1)
print(locate(l1,1))
print(count(l2,4))
print(reverse(l2))
print(isIncreasing(l1))
print(isIncreasing(l3))
print(palindrome(l1))
print(palindrome(l4))
print(palindrome(l5))

