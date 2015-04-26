
# Water Color


# This program draws randomly colored fading dots that are
#	placed by the mouse clicks of the user.  

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# Global Variables

canvas_width = 300
canvas_height = 300
dots = []
WDOTS = []

# Classes for colors and dots


class RGBcolor:
    
    # create color with specified intensities
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    # make HTML color string
    def make_html(self):
        return "rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"
    
    # print out readable representation
    def __str__(self):
        return "Red: " + str(self.red) + ", Green: " + str(self.green) + ", Blue: " + str(self.blue)
    
    # brighten towards white
    def brighten(self):
        self.red += 1
        self.green += 1
        self.blue += 1
        
class Dot:
    def __init__(self, pos, color, radius, lifespan):
        self.pos = pos
        self.color = color
        self.radius = radius
        # Without lifespan, the number of dots would increase
        #   indefinitely, causing the program to slow down.
        self.life = lifespan
        
    def draw(self, canvas):
        color_string = self.color.make_html()
        canvas.draw_circle(self.pos, self.radius, 1, color_string, color_string)
        
    # Updates the life and causes the color to fade to white.
    def update(self):
        self.life -= 1
        self.color.brighten()
        self.radius += 0.1
        #print self.color
    def get_life(self):
        return self.life     
        
class WDot:
    def __init__(self, pos, color, radius, lifespan):
        '''lifespan as color steps... 
        '''
        self.pos = pos
        self.color = color 
        self.radius = radius
        # Without lifespan, the number of dots would increase
        #	indefinitely, causing the program to slow down.
        self.life = lifespan
        self.dots = []
        self._gen_dots()
           
    def draw(self, canvas):
        for w in self.dots:
            print w
            #color_string = self.color.make_html()
            #  [(187, 216), 26.6, 1, 'rgb(338, 374, 415)', 'rgb(338, 374, 415)']
            canvas.draw_circle(w[0]
                          , w[1]
                          , 1
                          , w[3]
                          , w[4]
                          )
        
   
    def _gen_dots(self):
        for d in range(self.life):
            self.color.brighten()
            color_string = self.color. make_html()
            self.dots.append([self.pos
                    , (self.radius +  (0.42 * d))
                    , 1
                    , color_string, color_string
           ])
        #d.draw(canvas) 
        self.dots.reverse()
        #for i in self.dots:
         #     print i
        
# updates the life and causes the color to fade to white.
    def update(self):
        self.life -= 1
        self.color.brighten()
        self.radius += 0.1
        #print self.color.reverse
               
    def get_life(self):
        return self.life


 
       

# Event Handlers
def draw(canvas):
    # iterate over list(dots) instead of dots, to make a copy.
    #this allows you to safely remoe from dots inside the loop.
    for d in list(dots):
        d.update()
        d.draw(canvas)
        #remove dot if it's too old
        if d.life <= 0:
            dots.remove(d)
                    
def wdraw(canvas):
    for d in list(WDOTS):
        #print d.dots
        d.draw(canvas)
    return None          
           
     
def click(pos):
    new_color = RGBcolor(random.randrange(0,256), random.randrange(0,256), 
         random.randrange(0,256))
    print new_color
    print "HTML color is " + new_color.make_html()
    print
    # dots.append(WDot(pos, new_color, 20, 256))
    WDOTS.append (WDot(pos, new_color, 7, 42))
    
# Frame
 
frame = simplegui.create_frame("Water Color", canvas_width, canvas_height) 

# Register Event Handlers

#frame.set_draw_handler(draw)
frame.set_draw_handler(wdraw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")

# Start
frame.start()