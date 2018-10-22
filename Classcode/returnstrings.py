def bondify(name):
    
    '''
takes in a string in the form first alst an return it in the form 'las, first last
'''
def bondify(name):
    space_index = name.find(' ')
    first = name[0:space_index]
    last = name[space_index+1:] #the +1 is for he space
    bond_name = last + ", " + first + " " +last
    return bond_name

print(bondify("Hello World"))
print(bondify("James Bond"))