'''
Name: Jiawen Cai
Class: CS 5001.17350.202410
This is for #3 Programming in HW2:Functions and Testings
'''

import turtle

turtle.Screen().bgpic("shape_window.png")

#create two objects
square_pen = turtle.Turtle()
circle_pen = turtle.Turtle()

#set reusable constants for different functions
square_side_length = 80
radius = 40

#function1: draw squares and cicles
def shapes_drawer():

    '''
    Function -- shapes_drawer
    Draws a green square and a blue circle using Turtle graphics.
    
    Parameters:
    None
    
    Precondition:
    - square_pen and circle_pen must be initialized as Turtle objects.
    - square_side_length and radius must be defined before calling this function.
    '''

    x, y = 0 - square_side_length/2, square_side_length/2
    
    square_pen.penup()
    square_pen.goto(x, y)
    square_pen.pendown()
    square_pen.pencolor("green")

    for _ in range(4):
        square_pen.forward(square_side_length)
        square_pen.right(90)

    circle_pen.penup()
    circle_pen.goto(0, 0-square_side_length/2)
    circle_pen.pendown()
    circle_pen.pencolor("blue")
    circle_pen.circle(radius)

#function2: clear the former square and circle
def clear_shapes():
    
    square_pen.clear()
    circle_pen.clear()

#function3: draw new square and circle according to input
def new_shapes_drawer(new_square_x, new_square_y, new_circle_x, new_circle_y):
    '''
    Function -- new_shapes_drawer
    Draws a new green square and a new blue circle at specified positions using Turtle graphics.
    
    Parameters:
    new_square_x -- the x-coordinate of the new square's top-left corner
    new_square_y -- the y-coordinate of the new square's top-left corner
    new_circle_x -- the x-coordinate of the new circle's center
    new_circle_y -- the y-coordinate of the new circle's center

    Draws a new green square and a new blue circle using Turtle graphics. The square
    is drawn with its top-left corner located at the specified position, and
    the circle is drawn centered at the specified position.

    This function utilizes the square_pen and circle_pen Turtle objects.

    Precondition:
    - square_pen and circle_pen must be initialized as Turtle objects.
    - square_side_length and radius must be defined before calling this function.
    
    '''
    square_pen.penup()
    square_pen.goto(new_square_x - square_side_length/2, new_square_y - square_side_length/2)
    square_pen.pendown()
    square_pen.fillcolor("green")
    square_pen.begin_fill()

    for _ in range(4):
        square_pen.forward(square_side_length)
        square_pen.left(90)

    square_pen.end_fill()

    circle_pen.penup()
    circle_pen.goto(new_circle_x, new_circle_y)
    circle_pen.pendown()
    circle_pen.fillcolor("blue")
    circle_pen.begin_fill()
    circle_pen.circle(radius)
    circle_pen.end_fill()
