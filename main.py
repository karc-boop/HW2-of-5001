import turtle
import align_drawer

def main():
    '''
    Function -- main
    Executes the program to draw and manipulate shapes using Turtle graphics.
    
    Parameters:
    None
    
    This function orchestrates the drawing and manipulation of shapes using Turtle graphics.
    It first draws initial shapes using shapes_drawer, clears the old shapes using clear_shapes,
    takes user input for new shape positions, draws new shapes using new_shapes_drawer, and
    displays the result on the screen.
    '''
    align_drawer.shapes_drawer()

    align_drawer.clear_shapes()
    
    new_square_x = int(input("Enter the x coordinate of the new square's position: "))
    new_square_y = int(input("Enter the y coordinate of the new square's position: "))
    new_circle_x = int(input("Enter the x coordinate of the new circle center's position: "))
    new_circle_y = int(input("Enter the y coordinate of the new circle center's position: "))

    align_drawer.new_shapes_drawer(new_square_x, new_square_y, new_circle_x, new_circle_y)

    turtle.done()

if __name__ == "__main__":
    main()

