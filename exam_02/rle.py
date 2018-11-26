##def encode(s):
##    l=[]  
##    for i in range(0,len(s)-1):
##        count = 1
##        x = True
##        y=1
##        while x is True and y < len(s)-1:
##            if s[i]==s[i+y]:
##                count+=1
##                y+=1
##            else:
##                x = False       
##        l.append([s[i],count])
##    return l
##        
##def encode(s):
##    l=[]  
##    for i in range(0,len(s)-1):
##        y=1
##        count=1
##        if s[i]==s[i+y]:
##            count+=1
##            y+=1      
##        l.append([s[i],count])
##    return l

def encode(s):
    l=[]
    x=1
    count=1
    for i in range(0,len(s)-1):
        if i == len(s)-1:
            l.append([s[i],count])
            return l
        while i+x < len(s)-1 and s[i]==s[i+x]:
                count+=1
                x+=1
        l.append([s[i],count])
    return l        
        
        
print("abb",encode("abb"))
##example = encode("abb")
print("abcd",encode("abcd"))
print("abccccccdd",encode("abccccccdd"))

def decode(l):
    word=[]
    for list in l:
        letter = list[0]
        times=list[1]
        i=0
        while i < times:
            word.append(letter)
            i+=1
    wordString="".join(word)
    return wordString        
##print(decode(example))