def happyLadybugs(b):
    for character in b:
        if character!= "_" and b.count(character) == 1:
            return "No"
    if b.count("_")==0:
        i = 0
        while i < (len(b)-1):
            if b[i] != b[i+1]:
                return "No"
            else:
                i+=1
        return "yes"
    else:
        return "yes"


print(happyLadybugs(["B","C"]))
print(happyLadybugs(["B","B"]))
print(happyLadybugs(["B","C","B"]))
print(happyLadybugs(["B","C","B","C","_"]))