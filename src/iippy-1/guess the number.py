 # "Guess the number" is not only a boring game but also a project we must finish...
 
 # import the modules
-import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
+import simplegui
 import random
 import math
 
-# Define global variables used in the code
-        
+# globla variable initialization
+num_range = 100
+secret_number = 0
+chance_left = 7
+
+# helper function to start and restart the game
+def new_game():
+    # initialize global variables used in your code here
+    global num_range
+    if num_range == 100:
+        range100()
+    elif num_range == 1000:
+        range1000()
+
+# define event handlers for control panel
 def range100():
     # button that changes the range to [0,100) and starts a new game
-    global secret_number, guess_chance
-    guess_chance = 7
-    secret_number = random.randint ( 0 , 100 )
+    global secret_number
+    global num_range
+    global chance_left
+    chance_left = 7
+    num_range = 100
+    secret_number = random.randrange ( 0 , 100 )
     print "Welcome to the boring game!"
-    print "Please input a number from 0 to 99 (:"
+    print "Please input a number from 0 to",num_range,"(-:"
     
 def range1000():
     # button that changes the range to [0,100) and starts a new game
-    global secret_number, guess_chance
-    guess_chance = 7
-    secret_number = random.randint ( 0 , 1000 )
-    print "Welcome to the boring game!"
-    print "Please input a number from 0 to 999 (:"
+    global secret_number
+    global num_range
+    global chance_left
+    chance_left = 10
+    num_range = 1000
+    secret_number = random.randrange ( 0 , 1000 )
+    print "Welcome to the boring game! \n"
+    print "Please input a number from 0 to",num_range,"(-:\n"
     
     
-def input_guess(num):
+def input_guess(guess):
     # main game logic goes here
-    global guess, guess_chance
-    guess = int(num)
-    guess_chance = guess_chance-1
-    print "Input number is", str(guess), "Chance", guess_chance
-    if   (guess > secret_number) and (guess_chance > 0):
-        print "Higher!"
-    elif (guess < secret_number) and (guess_chance > 0):
-        print "Lower!"
-    elif (guess == secret_number) and (guess_chance > 0):
-        print "Correct! Yeah~"
+    global secret_number
+    global chance_left
+    chance_left = chance_left - 1
+    if str.isdigit(guess):
+        print "Input number is " + guess,".\n"
+        if int(guess) == secret_number:
+            print "Correct! Yeah~ \n"
+            int()
+        elif  int(guess) > secret_number and chance_left > 1:
+            print "Lower,please! \n"
+            print "And there are",chance_left,"chances left. \n"
+        elif  int(guess) > secret_number and chance_left == 1:
+            print "Lower,please! \n"
+            print "And there is",chance_left,"chance left. \n"
+ 
+        elif int(guess) < secret_number and chance_left > 1:
+            print "Higher,please! \n"
+            print "And there are",chance_left,"chances left.\n"
+        elif int(guess) < secret_number and chance_left == 1:
+            print "Higher,please! \n"
+            print "and there is",chance_left,"chance left.\n"
+        if  chance_left == 0:
+             print "Game over! The Right Number is", secret_number,"\n"
+             new_game()
     else :
-        print "Game over! The number is",secret_number
+        print "Invalid entry. Please enter a number in range.","\n"
 
 # create window(s)
-frame = simplegui.create_frame("Guess the number", 200, 200)
-
-# create control elements for window，
-#2 event handlers for the buttons
-#1 event handler for the input field）
+frame = simplegui.create_frame("Guess the Number", 200, 200)
 
 # register event handlers for control elements and start frame
-frame.add_button("Range is 0~100", range100, 200)
-frame.add_button("Range is 0~1000", range1000, 200)
-frame.add_input("Enter a guess", input_guess, 200)
+frame.add_button("Range is [0,100)", range100, 150)
+frame.add_button("Range is [0,1000)", range1000, 150)
+frame.add_input("Enter the Number You Guess", input_guess, 200)
 
 # start handlers for created window and exit code
-# always remember to check your completed program against the grading rubric
\ No newline at end of file
+frame.start()
+# start a new game
+new_game()
+# always remember to check your completed program against the grading rubric
