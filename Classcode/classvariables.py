def is_odd(n):
    return n%2==1
def is_even(n):
    return n%2==0
def is_big(n):
    return n>5
def myfilter(predicate,l):
    result =[]
    for item in l:
        if predicate(item):
            result.append(item)
    return result
l = [1,2,7,8]
print(myfilter(is_odd, l))

sentence="when shall we three meet again"
wl = sentence.split()
" ".join(wl) #puts space in bw each item in list and turns it into a stringS
#