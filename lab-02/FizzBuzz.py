
def fizzBuzz(number):
    x=1
    while x<=number:
        if x % 15 == 0:
            print("\nFizzBuzz")
        elif x % 5 ==0:
            print("Buzz")
        elif x % 3 ==0:
            print ("Fizz")
        else:
            print(x)
        x=x+1
  
        

        
print(fizzBuzz(100))