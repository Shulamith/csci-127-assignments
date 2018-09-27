#hw3 Darren Zou and Shulamith Dashevsky
#in the lop print out thesequence
#return and print out the # of steps
def collatz(int):
    steps = 0
    while (int != 1):
        if (int % 2 == 0):
            steps += 1
            int = int/2
            print(int)
        else:
            steps += 1
            int = (int * 3) + 1
            print(int)
    print("it took:", steps, "steps")
     
    
    
print(collatz(100))