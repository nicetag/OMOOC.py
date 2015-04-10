# "Guess the number" is not only a boring game but also a project we must finish...

# import the modules
import simplegui
import random
import math

# Define global variables used in the code
        
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number, guess_chance
    guess_chance = 7
    secret_number = random.randint ( 0 , 100 )
    print "Welcome to the boring game!"
    print "Please input a number from 0 to 99 (:"
    
def range1000():
    # button that changes the range to [0,100) and starts a new game
    global secret_number, guess_chance
    guess_chance = 7
    secret_number = random.randint ( 0 , 1000 )
    print "Welcome to the boring game!"
    print "Please input a number from 0 to 999 (:"
    
    
def input_guess(num):
    # main game logic goes here
    global guess, guess_chance
    guess = int(num)
    guess_chance = guess_chance-1
    print "Input number is", str(guess), "Chance", guess_chance
    if   (guess > secret_number) and (guess_chance > 0):
        print "Higher!"
    elif (guess < secret_number) and (guess_chance > 0):
        print "Lower!"
    elif (guess == secret_number) and (guess_chance > 0):
        print "Correct! Yeah~"
    else :
        print "Game over! The number is",secret_number

# create window(s)
frame = simplegui.create_frame("Guess the number", 200, 200)

# create control elements for window，
#2 event handlers for the buttons
#1 event handler for the input field）

# register event handlers for control elements and start frame
frame.add_button("Range is 0~100", range100, 200)
frame.add_button("Range is 0~1000", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# start handlers for created window and exit code
# always remember to check your completed program against the grading rubric
 No newline at end of file
