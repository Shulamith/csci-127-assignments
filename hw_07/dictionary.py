import random
sentence = "<firstname> Reeves, whose first name means <adj> <noun> over the <noun> in Hawaiian, <verb> for a living."
sentenceTwo = "<hero> <verb> in the <noun> and then <hero> <verb> <noun> later."
POS={}
POS={'firstnames': ["Kasandra", "Ying", "Sam", "Michael"],
'adjectives': ["swift", "fast", "fiery", "many", "blue", "sad", "joyous"],
'nouns':["car", "mountain", "sky", "star", "wolf", "dog", "shoe", "watch"],
'verbs':["meditates", "works", "runs", "plays", "sings", "spits", "explodes"],
'heros': ["Spiderman", "Wonderwoman", "Thor", "Batman"]}


def madlibs(s,d):
    newS=[]
    heroN=random.choice(d['heros']) 
    #make a list that holds all the bracketed stuff
    madlibList = s.split()
    for item in madlibList:
        if item == "<firstname>":
            newS.append(random.choice(d['firstnames']))
        elif item == "<adj>":
            newS.append(random.choice(d['adjectives']))
        elif item == "<noun>":
            newS.append(random.choice(d['nouns']))
        elif item == "<verb>":
            newS.append(random.choice(d['verbs']))
        elif item == "<hero>":
            newS.append(heroN)
        else:
            newS.append(item)
    sentenceString = " ".join(newS)
    return sentenceString.capitalize()
print(madlibs(sentence,POS))
print(madlibs(sentenceTwo,POS))