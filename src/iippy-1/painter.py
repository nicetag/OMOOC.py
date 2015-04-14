
# import modules

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

#find globals
WIDTH = 500
HEIGHT = 500
paint_shape = "circle"
paint_color = "Lightgrey"
pos = [WIDTH / 2, HEIGHT / 2]
radius = 25
shape_list = []

#define event handler for mouse click, paint

#mouse click 
def click(position):
    global pos, shape_list
    pos = list(position)
    shape_list.append([pos,paint_shape,paint_color])
    
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
    global paint_shape
    paint_shape = "circle"

def draw_square():
    global paint_shape
    paint_shape = "square"

def draw_triangle():
    global paint_shape
    paint_shape = "triangle"

#canvas
def draw(canvas):
    draw_pos = list(pos)
    x = pos[0]
    y = pos[1]
    r = radius
    
    if paint_shape == "triangle":
       canvas.draw_polygon([(x,y+r),(x-r,y-r/2),(x+r,y-r/2)], 1, "White", paint_color)
    elif paint_shape == "square":
       canvas.draw_polygon([(x-r, y-r),(x-r, y+r),(x+r, y+r),(x+r, y-r)],1,"White",paint_color)
    elif paint_shape == "circle":
       canvas.draw_circle(draw_pos, radius ,1, "White", paint_color)

# record in list
    for draw_pos in shape_list:
        if draw_pos[1] == "circle":
            canvas.draw_circle(draw_pos[0], radius,1, paint_color, draw_pos[2])
        else:
            canvas.draw_polygon(draw_pos[0], 1, paint_color, draw_pos[2])
  
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

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

#start frame 
frame.start()




            
