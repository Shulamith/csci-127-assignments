def encode(s):
    l=[]  
    for i in range(0,len(s)-1):
        count = 1
        x = True
        y=1
        while x is True and y < len(s)-1:
            if s[i]==s[i+y]:
                count+=1
                y+=1
            else:
                x = False
                l.append([s[i],count])
    return l
        
    
print("abb",encode("abb"))
print("abcd",encode("abcd"))

def decode(l):
    
