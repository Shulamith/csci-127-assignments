##d = {2:['Hello']}
##d[2].append('retro')
##print(d)



d={}
def addline(d,line):
    lowercase = line.lower();
    words = lowercase.split();
    for word in words:
        if word[0] in d:
            d[word[0]].append(word);
        else:
            d[word[0]] = [word];
    return d
print(addline(d,"hello My Name iS Holmes"))
addline(d,"For me to rap like a computer must be in my genes")
addline(d, "I got a laptop in my back pocket")
addline(d,"her hardest HUE to hold")
addline(d,"her early leaf's a flower")
addline(d,"Thank you, NEXT")
print(d)


def spellcheck(d,word):
    lowercase= word.lower();
    if lowercase[0] in d and lowercase in d[lowercase[0]]:
        return True
    else:
        return False
    
print("RAp",spellcheck(d,"RAp"))
print("Holmes",spellcheck(d,"Holmes"))
print("asdlfjksdfl",spellcheck(d,"asdlfjsdlf"))
print("um",spellcheck(d,"um"))
print("laptop",spellcheck(d,"laptop"))
##print("RAp",spellcheck(d,"RAp"))

    
    