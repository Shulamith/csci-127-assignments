#if blank blank called boolean expression (something that can be answered as true and false)
import random
if True:
    print("this always executes")
    print ("multiple lines can excute if the boolean condition is true")
if False:
    print("this never excutes")

if 5>3:
    print("boolean is true")
if 5!=5:
    print("above boolean is true")
name="Joe"
if name.upper()=="joe".upper():
    print("hi Joe")
    
if False == False:
    print("This can be tricky")
if not True == False:
    print("this is the same thing")
number = random.randrange(10)
print("number = ",number)
if number >= 5:
    print ("number is greater than 5:", number)
elif number>4:
    print("number is greater than four but than 7:", number)
else:
    print("number <=4", number)
    