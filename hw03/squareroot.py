#or sqrt.py
#(old guess + n/oldguess) /2
##def mySquareroot(number):
##    guess = 5
##    while ((guess * guess) != number):
##        if (number / guess > guess):
##            guess +=1
##        elif guess
##        
        
def mySquareroot(number):
    guess = 5
    i = 1
##    oldguess = 0
    print("This is my first guess:")
    while ((guess * guess) != number and i<=20): #either if perfect square or if python continues to repeat the same guess
##        oldguess = guess
        print(guess)
        guess = ((guess + (number/guess))/2)
        i +=1
    guess = str(round(guess, 2))
    print(guess) 
    print("The above is either the answer or the closest we can to this function")
        
##   if (i=20):
##       print ("There is no ration sqrt. It is approximatley...")
print(mySquareroot(16))
print(mySquareroot(1003))
