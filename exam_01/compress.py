vowels = ['a', 'i', 'o', 'u', 'e']
##def compress_word(w):
##    word = w.split()
##    i=0
##    newword =[]
##    newword.append(word[i])
##    print(word[i])
##    i+=1
##    while i<(len(word)):
##        if word[i] in vowels:
##         i+=1
##        else:
##            newword.append(word[i])
##    return newword
##
##



def compress_word(w):
    i=1
    newWord = []
    for character in w:
        if character in vowels:
            pass
        else:
            newWord.append(character)
            actualnewWord = ''.join(newWord)
    return actualnewWord
        

print("halloween becomes:",compress_word("halloween"))
print("orange becomes:",compress_word("orange"))

def sentence(line):
    newSentence = []
    sentence_list = line.split()
    for word in sentence_list:
        newSentence.append(compress_word(word))
    return ' '.join(newSentence)
        
print("I love riding my bike beocmes:",sentence("I love riding my bike"))
print("What do you mean? becomes:",sentence("What do you mean?"))
        
        