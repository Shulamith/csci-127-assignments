l=[2,7,9,0,8,0]
l1=[1,7,9,10]
l2=[1,2,3,2,1]
def locate(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            return i
        else:
            i+=1
    return -1
    
print(locate(l,8))
print(locate(l,1))

def count(list,value):
    i = 0
    count=0
    while i < len(list):
        if list[i] == value:
            count +=1
        else:
            pass
        i+=1
    return count

print(count(l,0))

def reverse(list):
    newlist=[]
    i=len(list)
    for item in list:
        newlist.append(list[i-1])
        i-=1
    return newlist

print(reverse(l))

def isIncreasing(list):
    i=0
    while i < len(list):
        if list[len(list)-1] > list[len(list)-2]:
            i+=1
        else:
            return False
    return True
def palindrome(list):
    i=1
    while i < len(list)/2:
        if list[i-1] == list[len(list)-i]:
            i+=1
        else:
            return False
    return True



print(palindrome(l2))
print(isIncreasing(l))
print(isIncreasing(l1))