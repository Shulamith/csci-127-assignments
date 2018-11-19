def makeacronym(w):
    acronym = []
    acronym.append(w[0])
    i=0
    for character in w:
        i+=1
        if character == ' ':
            acronym.append(w[i])
    acronymW = "".join(acronym)
    return acronymW
            

print("hello my name is:",makeacronym("hello my name is"))
print("See ya:",makeacronym("See ya"))
print("Laughing out loud:",makeacronym("Laughing out loud"))
print("What Do You Mean:",makeacronym("What Do You Mean"))
print("in my humble opinion:",makeacronym("in my humble opinion"))
print("don't worry:",makeacronym("don't worry"))
print("no problem:",makeacronym("no problem"))
print("No:",makeacronym("No"))
