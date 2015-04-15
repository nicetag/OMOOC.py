
# import modules

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

#find globals
WIDTH = 500
HEIGHT = 500
shape = "circle"
paint_color = "Lightgrey"
pos = [WIDTH / 2, HEIGHT / 2]
radius = 25
shape_list = []
be = 0
end = 1
n = 0
review = False

#define event handler for mouse click, paint

#mouse click 
def click(position):
    global pos, shape_list,end,n
    pos = list(position)
    shape_list.append([pos,shape,paint_color])
#settings for review
    end += 1
    n = 0
    review = False  
    
# function for review
def review1():
    global n, review
    review = True
    n += 1  

#colors and shapes
#colors
def paint_lightgrey():
    global paint_color
    paint_color = "Lightgrey"
    
def paint_silver():
    global paint_color
    paint_color = "Silver"

def paint_blue():
    global paint_color
    paint_color = "Blue"

#shapes
def draw_circle():
    global shape
    shape = "circle"

def draw_square():
    global shape
    shape = "square"

def draw_triangle():
    global shape
    shape = "triangle"
    
    if shape == "triangle":
         canvas.draw_polygon([(x,y+r),(x-r,y-r/2),(x+r,y-r/2)], 1, "white", paint_color)
    elif shape == "square":
         canvas.draw_polygon([(x-r, y-r),(x-r, y+r),(x+r, y+r),(x+r, y-r)],1,"white",paint_color)
    elif shape == "circle":
         canvas.draw_circle(draw_pos, radius ,1,"white", paint_color)


# record in list
draw_pos = list(pos)
x = pos[0]
y = pos[1]
r = radius
def draw(canvas):  
    if review == False :
       for draw_pos in shape_list[be:end]:     
          if draw_pos[1] == "circle":
             canvas.draw_circle(draw_pos[0], radius,1, "white", draw_pos[2])
          else:
             canvas.draw_polygon(draw_pos[0], 1, "white", draw_pos[2])
    else :
        for draw_pos in shape_list[be:end-n]:
           if draw_pos[1] == "circle":
             canvas.draw_circle(draw_pos[0], radius,1, "white", draw_pos[2])
           else:
             canvas.draw_polygon(draw_pos[0], 1, "white", draw_pos[2])
  
# Create frames and assign callbacks to event handlers

##create frame and set color and canvas
frame = simplegui.create_frame("The Painter", WIDTH, HEIGHT)
frame.set_canvas_background("white")

frame.add_button("circle",draw_circle,100)
frame.add_button("square", draw_square,100)
frame.add_button("triangle", draw_triangle,100)
frame.add_button("lightgrey", paint_lightgrey,100)
frame.add_button("silver", paint_silver,100)
frame.add_button("blue", paint_blue,100)
frame.add_button("review", review1, 100)

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

#start frame 
frame.start()




            
