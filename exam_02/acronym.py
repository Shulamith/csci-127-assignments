def makeacronym(w):
    acronym = []
    acronym.append(w[0])
    i=0
    for character in w:
        i+=1
        if character == ' ':
            acronym.append(w[i])
##    acronymW = acronym.join(" ")
    return acronym
            

print(makeacronym("hello my name is"))