#lab --make sure to write correct file name!! and folder
##madlib= "<exclamation> he said <Adverb> as he jumped into his <noun> and drove off with his <adjective> wife."
##NOUNS = ["car", "dog", "hammer"]
##def func_that_uses_NOUNS():
##    global NOUNS
import random    
#could make it more complex that adj and verbs would change but lets say a persons name wouldn't change
    
sentence = "<firstname> Reeves, whose first name means <adj> <noun> over the <noun> in Hawaiian, <verb> for a living."
sentenceTwo = "<hero> <verb> in the <noun> and then <hero> <verb> <noun> later."
##madliblist = split.sentence()
firstnames = ["Kasandra", "Ying", "Sam", "Michael"]
adjectives = ["swift", "fast", "fiery", "many", "blue", "sad", "joyous"]
nouns = ["car", "mountain", "sky", "star", "wolf", "dog", "shoe", "watch"]
verbs = ["meditates", "works", "runs", "plays", "sings", "spits", "explodes"]
heros=["Spiderman", "Wonderwoman", "Thor", "Batman"]

##partsofspeech=["firstnames", "adjectives", "nouns", "verbs", "hereos"]

##def madlibs(s):
###function that finds all the missing words    
###function that randomly chooses the items
###function that replaces all the <> with the item
###
##    madliblist = s.split()
##    for item in madliblist:
##        s = s.replace("<firstname>", random.choice(firstnames))
##        s = s.replace("<adj>", random.choice(adjectives))
##        s = s.replace("<noun>", random.choice(nouns))
##        s = s.replace("<verb>", random.choice(verbs))
##    return s
##print(madlibs(sentence))
def madlibs(s):
    newS=[]
    heroN=random.choice(heros)
    #make a list that holds all the bracketed stuff
    madlibList = s.split()
    for item in madlibList:
        if item == "<firstname>":
            newS.append(random.choice(firstnames))
        elif item == "<adj>":
            newS.append(random.choice(adjectives))
        elif item == "<noun>":
            newS.append(random.choice(nouns))
        elif item == "<verb>":
            newS.append(random.choice(verbs))
        elif item == "<hero>":
            newS.append(heroN)
        else:
            newS.append(item)
    sentenceString = " ".join(newS)
    return sentenceString.capitalize()
print(madlibs(sentence))
print(madlibs(sentenceTwo))

##def list_parts_of_speech(sentence):
##    for character in sentence:
##        if character = "<":
##        index = 
    




