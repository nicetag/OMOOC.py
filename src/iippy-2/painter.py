
# import modules

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

#find globals
WIDTH = 500
HEIGHT = 500
shape_list = []

# helper functions

# Handler to draw on canvas
def draw(canvas):
    global draw_pos, paint_shape, shape_radius, paint_color
    for draw_pos in shape_list:
        if draw_pos[1] =="circle":
            canvas.draw_circle(draw_pos[0], shape_radius,1,"White", draw_pos[2])
        else:
            canvas.draw_polygon(draw_pos[0], 1 , "White", draw_pos[2])

#helper functions
#canvas
def draw(canvas):
    global paint_color,paint_shape, draw_pos, shape_radius
    for draw_pos in shape_list:
        if draw_pos[1] =="circle":
            canvas.draw_circle(draw_pos[0], shape_radius,1,"White", draw_pos[2])
        else:
            canvas.draw_polygon(draw_pos[0], 1 , "White", draw_pos[2])
#shape and color
#shapes
def draw_circle():
    global paint_shape
    paint_shape = "circle\n"

def draw_square():
    global paint_shape
    paint_shape = "square\n"
def draw_triangle():
    global paint_shape
    paint_shape = "triangle\n"

#colors
def paint_lightgrey():
    global paint_color
    paint_color = "Lightgrey\n"

def paint_silver():
    global paint_color
    paint_color = "Silver"

def paint_blue():
    global paint_color
    paint_color = "Blue"

#define event handler for mouse click, paint
def click(pos):
    global draw_pos, paint_shape, shape_radius, paint_color, timer

# define timer
def timer_handler():
    global draw_pos,shape_list, order, step
        shape_list = []


# Create frames and assign callbacks to event handlers

##create frame and set color and canvas
frame = simplegui.create_frame("The Painter", WIDTH, HEIGHT)
frame.set_canvas_background("white")


frame.add_button("circle\n",draw_circle,100)
frame.add_button("square\n", draw_square,100)
frame.add_button("triangle\n", draw_triangle,100)
frame.add_button("lightgrey\n", paint_lightgrey,100)
frame.add_button("silver\n", paint_silver,100)
frame.add_button("blue\n", paint_blue,100)

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

#start frame & timers

frame.start()
timer.start()





