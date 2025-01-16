import turtle
from Helper import helper as util


def init_turtle(color,speed):
    """ This function initializas the trutle and is reuseable incase we have to make multiple turtles"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.left(90)  
    t.color(color)
    t.speed(speed)  
    t.penup()
    t.goto(0, -200) 
    t.pendown()
    return t,screen

def close_turtle(t,screen,branch_length):
    t.color("brown")
    t.forward(branch_length) 
    t.hideturtle()    
    screen.exitonclick()
    
def draw_tree(t, branch_length, left_angle, right_angle, depth, max_depth, reduction_factor):
    """Draws a tree using recursion."""
    if depth == 0:
        return
    
    if depth != max_depth:
        t.color("green")
    t.pensize(depth)
    t.forward(branch_length)    
    t.left(left_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle,right_angle, depth-1,max_depth, reduction_factor)
    t.right(right_angle + left_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle,right_angle, depth-1,max_depth, reduction_factor)
    t.left(right_angle)
    t.backward(branch_length)

def main(): 
    left_angle = util.get_valid_float("Enter left branch angle: ")
    right_angle = util.get_valid_float("Enter right branch angle: ")
    branch_length = util.get_valid_float("Enter starting branch length: ")
    recursion_depth = util.get_valid_int("Enter recursion depth: ")
    reduction_factor = util.get_valid_int("Enter branch length reduction percent (0-100) : ",0,100)
    
  
    t1,screen = init_turtle("brown",0)    
    draw_tree(t1, branch_length, left_angle, right_angle, recursion_depth,recursion_depth, reduction_factor/100) 
    close_turtle(t1,screen,branch_length)   
   

if __name__ == "__main__":
    main()
