# "Guess the number" is not only a boring game but also a project we must finish...

# import the modules
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

# globla variable initialization
num_range = 100
secret_number = 0
chance_left = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global num_range
    global chance_left
    chance_left = 7
    num_range = 100
    secret_number = random.randrange ( 0 , 100 )
    print "Welcome to the boring game!"
    print "Please input a number from 0 to",num_range,"(-:\n"

def range1000():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global num_range
    global chance_left
    chance_left = 10
    num_range = 1000
    secret_number = random.randrange ( 0 , 1000 )
    print "Welcome to the boring game! \n"
    print "Please input a number from 0 to",num_range,"(-:\n"


def input_guess(guess):
    # main game logic goes here
    global secret_number
    global chance_left
    chance_left = chance_left - 1
    if str.isdigit(guess):
        print "Input number is " + guess
        if int(guess) == secret_number:
            print "Correct! Yeah~ \n"
            new_game()
        elif  0 < int(guess) < num_range and int(guess) > secret_number and chance_left > 1:
            print "Lower,please!"
            print "And there are",chance_left,"chances left. \n"
        elif  0 < int(guess) < num_range and int(guess) > secret_number and chance_left == 1:
            print "Lower,please!"
            print "And there is",chance_left,"chance left. \n"
        
        elif 0 < int(guess) < num_range and int(guess) < secret_number and chance_left > 1:
            print "Higher,please!"
            print "And there are",chance_left,"chances left.\n"
        elif 0 < int(guess) < num_range and int(guess) < secret_number and chance_left == 1:
            print "Higher,please!"
            print "and there is",chance_left,"chance left.\n"
        elif chance_left == 0:
            print "Game over! The Right Number is", secret_number,"\n"
            new_game()
        else :
            print "Please enter a number in range."
            print "And there are",chance_left,"chances left.\n"
    elif chance_left > 1:
        print "Invalid entry. Please enter a number in range."
        print "And there are",chance_left,"chances left.\n"
    elif chance_left == 1:
        print "Invalid entry. Please enter a number in range."
        print "and there is",chance_left,"chance left.\n"
    elif chance_left == 0:
        print "Game over! The Right Number is", secret_number,"\n"
        new_game()

# create window(s)
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 150)
frame.add_button("Range is [0,1000)", range1000, 150)
frame.add_input("Enter the Number You Guess", input_guess, 200)

# start handlers for created window and exit code
frame.start()
# start a new game
new_game()
# always remember to check your completed program against the grading rubric
