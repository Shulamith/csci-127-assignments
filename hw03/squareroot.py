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
    while ((guess * guess) != number and i<20):
        print(guess)
        guess = ((guess + (number/guess))/2)
        i +=1
        
   if (i=20):
       print ("There is no ration sqrt. It is approximatley...")
print(mySquareroot(16))
print(mySquareroot(19))