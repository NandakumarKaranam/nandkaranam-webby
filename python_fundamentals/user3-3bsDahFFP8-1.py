# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#importing required libraries
import random
import simplegui
import math


# initialize global variables used in your code
# global variables initialized to default numbers
secret_number = random.randrange(0, 101)
user_guess = 15
# flag decides range
flag = 0
#number of attempts by user
attempt = 1
# number of attempts allowed
n = 7

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global flag
    print ""
    flag = 0
    num_attempts()
    secret_number = random.randrange(0, 101)
    print "New Game:Guess the number between 0 to 100"   
    print "Number of Guesses remaining",n
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    global flag
    flag = 1
    num_attempts()
    print ""
    secret_number = random.randrange(0,1001)
    print "New Game:Guess the number between 0 to 1000"
    print "Number of Guesses remaining",n
    
    
def get_input(guess):
    # main game logic goes here	
    global attempt, n
    num = int(guess)
    print ""
    print "Guess was",num
    print "Number of Guesses remaining",n-attempt
    
    if not (n-attempt) == 0:
        
        attempt = attempt + 1
        if(num > secret_number):
            print "Higher!!"
        elif(num < secret_number):
            print "Lower!!"
        else:
            print "Correct!!"
            restart()
           
    else:
        print ""
        print "Sorry",n,"attempts are over!!"
        print "try again"
        restart()
                
            

#restarts the game        
def restart():
    global flag, attempt
    attempt = 1
    if(flag == 1):
        range1000()
    else:
        range100()

#calculates the number of guesses for a range, based on
#binary search algorithm
def num_attempts():
    global flag, n
    if flag:
        n = math.ceil(math.log(1000)/math.log(2))
    else:
        n = math.ceil(math.log(100)/math.log(2))
        
            

    
# create frame
frame = simplegui.create_frame("Testing", 200, 200)


# register event handlers for control elements
Button1 = frame.add_button("In range 0 to 100", range100, 100)
Button2 = frame.add_button("In range 0 to 1000", range1000, 100)
Button3 = frame.add_button("Restart", restart, 100)
inp = frame.add_input("Guess", get_input, 200)

# start frame
frame.start()
range100()
num_attempts()

# always remember to check your completed program against the grading rubric
#checked ^^
