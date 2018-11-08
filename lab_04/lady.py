#python allows you to hold integers and strings in list but most don't usually only dictionary/hashmaps/keyvalue pairs/map/hashtable

def happyLadybugs(b):
    for character in b:
        if character!= "_" and b.count(character) == 1:
            return "No"
    if b.count("_")==0:
        i = 0
        while i < (len(b)-1): #alternatively fo i in inrange(0, len(b)-1)
            if b[i] != b[i+1]:
                return "No"
            else:
                i+=1
        return "yes"
    else:
        #I really should try to make the thing here
        #I wonder f I could see minimum amount of spaces rel to list needed to ensure possibility or to ensure that it is not solvable"
        return "yes"


print("B,C",happyLadybugs(["B","C"]))
print("B,B",happyLadybugs(["B","B"]))
print("B,C,B",happyLadybugs(["B","C","B"]))
print('B,C,B,C,_',happyLadybugs(["B","C","B","C","_"]))
print("B","_","C","A","B","C","A",happyLadybugs(["B","_","C","A","B","C","A"]))