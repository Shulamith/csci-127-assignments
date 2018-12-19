def makeacronym(phrase):
    acronym = []
    acronym.append(phrase[0])
    x=0;
    while x < len(phrase):
        if phrase[x] == " ":
            acronym.append(phrase[x+1])
            x+=1;
        else:
            pass
            x+=1
    acr = "".join(acronym)
    return acr
        

print(makeacronym("Hi My Name Is"))
print(makeacronym("don't worry"))
print(makeacronym("in my humble opinion"))
print(makeacronym("i"))
