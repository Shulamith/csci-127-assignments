tupleOne=('A','E','I','O','U','L','N','R','S','T')
tupleTwo=('D','G')
tupleThree=('B','C','M','P')
tupleFour=('F','H','V','W','Y')
tupleFive=('K')
tupleEight=('J','X')
tupleTen=('Q','Z')
##d = {tupleOne:1,tupleTwo:2,tupleThree:3,tupleFour:4,tupleFive:5,tupleEight:8,tupleTen:10}
##def score(w):
##    points=0
##    for letter in w:
##        point = d.get(letter) 
##        print (point)
##        
##print(score("HELLO"))

d = {'A':1,'E':1,'I':1,'O':1,'U':1,'L':1,'N':1,'R':1,'S':1,'T':1,'D':2,'G':2,'B':3,'C':3,'M':3,'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':10,'Z':10}
def score(w):
    points=0
    for letter in w:
        point = d.get(letter) 
        points=points+point
    return points
        
print("HELLO",score("HELLO"))
print("A",score("A"))
print("ENCYCLOPEDIA",score("ENCYCLOPEDIA"))
print("ZEBRA",score("ZEBRA"))
print("QUEUE",score("QUEUE"))
print("JUG",score("JUG"))