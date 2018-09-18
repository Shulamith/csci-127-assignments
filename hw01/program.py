def capitalize(name):
    space_index = name.find(' ')
    first = name[0:space_index] #could use not 
    last = name[space_index+1:]
    return(first.capitalize() + " " + last.capitalize())
print("I entered johnny appleseed and recieved...")    
print(capitalize("johnny appleseed"))


def capitalizeTwo(name): ##this is an additional way I found on stack overflow that makes it really simply
    return(name.title()) #it capitilizes the first letter follwing a space, but caution because it will make anything else lowercase so McDonald won't work
#this is an additional way I found on stack overflow that makes it really simple
#it capitilizes the first letter follwing a space,
#but caution because it will make anything else lowercase so McDonald won't work
print("\nsecond option...")
print(capitalizeTwo("firstnameversiontwo lastname"))


def init(name):
    space_index = name.find(' ')
    first = name[0] + "."
    last = name[space_index+1:]
    return(first.capitalize() + " " + last.capitalize())
print("\nI entered alan turing and recieved...")
print(init("alan turing"))

def part_pig_latin(word):
    return(word[1:] + word[0] + "ay")
print("\nDo you speak Pig Latin because I...")
print(part_pig_latin("speak"))

def make_out_word(out, word):
  return(out[0:2] + word + out[2:])
print("\nCoding bat example: test bat")
print (make_out_word("test", "bat"))

def make_tags(tag, word):
  return('<' + tag + '>' +word+ '</'+tag+'>')
print("\nmake tags. Ex tag i and word important")
print(make_tags("i", "important"))