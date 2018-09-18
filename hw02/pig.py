
#Nursima Donuk and Shulamith Dashevsky
vowels = ["a", "i", "o", "u", "e"]
def pig_latinify(word):
    if word[0] in vowels:
        return word+"ay"
    else:
        return word[1:] + word[0] + "ay"
print("When you want to say under say...") 
print (pig_latinify("under"))
print("when you want to say hello say...")
print(pig_latinify("hello"))

##
##def pig_latinVersionTwo(wordT):
##    if (wordT[0] != "a" or wordT[0]!="e" or wordT[0]!="i" or wordT[0]!="o" or wordT[0]!="u"):
##        return wordT[1:] + wordT[0] + "ay"     
##    else:
##        return wordT+"ay"





##
##def pig_latinVersionTwo(word):
##    if word[0] == "a":
##        vowel = True
##    elif word[0] == "e" :
##        vowel = True
##    elif word[0] == "i":
##        vowel = True
##    elif word[0] == "o":
##        vowel = True
##    elif word[0] == "u":
##        vowel = True
##    else:
##        return word[1:] + word[0] + "ay"
##    if vowel == True:
##        return word+"ay"
##print(pig_latinVersionTwo("hello"))
##print(pig_latinVersionTwo("under"))


def pig_latinVersionTwo(word):
    if word[0] == "a" or word[0] == "e" or word[0] =="i" or word[0] == "o" or word[0] == "u":
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"
print("This is the second way of doing it with the or statment and not the list")
print(pig_latinVersionTwo("hello"))
print (pig_latinVersionTwo("under"))