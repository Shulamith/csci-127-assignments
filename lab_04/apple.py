#s is the left border of the house
#t is the right border of the house
#a is the location of the apple tree
#b is the location of the orange tree
#apples is the list that contains how far each apple was thrown from the tree and in which directin
#oranges is the same as apples but for oranges

def countApplesandOranges(s,t,a,b,apples,oranges):
    a_on_house=0
    b_on_house=0
    for distance in apples:
        distance +=a
        if distance >=s and distance <=t:
            a_on_house+=1
    for distance in oranges:
        distance +=b
        if distance >=s and distance <=t:
            b_on_house+=1
    return "Apples: " + str(a_on_house)+"\nOranges:" +str(b_on_house)

       
print("original example",countApplesandOranges(7,10,4,12,[2,3,-4],[3,-2,-4]))
print("Same, but distance in the negatives",countApplesandOranges(-3,-1,4,12,[2,3,-4],[3,-2,-4]))
print("Five Apples thrown",countApplesandOranges(-3,7,4,12,[2,3,-4,-10,4],[3,-2,-4,5,-6]))