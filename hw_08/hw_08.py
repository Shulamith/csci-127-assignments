filename = "moby-small.txt"
filenameTwo = "moby-medium.txt"
filenameThree = "moby-large.txt"
s = 'one two three four five four six three seven three two three eight nine'

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d
def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result
##d=build_word_counts(s)
##print(d)
f = open(filename)
s = f.read()
words_uncleaned = build_word_counts(s)
print(words_uncleaned)
cleaned_string = clean_data(s)
print(cleaned_string)
print("-------------------")
words = build_word_counts(cleaned_string)
print(words)
common_words=[]
vals = words.values()
vals = sorted(vals)
##print(vals)
##for k in words:
##    if words[k]>1000:
##        common_words.append([k,words[k]])

def build_phrases(cleaned_string):
    clean_list=cleaned_string.split()
    new_d={}
   
    for i in range(0,len(clean_list)-1):
        #print(word)
        new_d.setdefault(clean_list[i],[]).append(clean_list[i+1])
        
    return new_d
        
        
        
        
        
print(build_phrases(cleaned_string))


        
               

##common_words = [ [k,words[k]]for k in words]

#interstingproject to consider: patterns in zen and the art of motorcycle, udit's poem, and most commmon music note beethoven

#make a dictionary with word and word after it:
#hw8
#Call:[me,it] me:[Ishmael] Ishmael:[some]