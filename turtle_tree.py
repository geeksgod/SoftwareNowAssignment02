import turtle


def draw_tree(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    
    if depth == 0:
        return
    
    if depth != 5:
        t.color("green")
    t.pensize(depth)
    t.forward(branch_length)    
    t.left(left_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle,right_angle, depth-1, reduction_factor)
    t.right(right_angle + left_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle,right_angle, depth-1, reduction_factor)
    t.left(right_angle)
    t.backward(branch_length)

def main(): 
    left_angle = float(input("Enter left branch angle: "))
    right_angle = float(input("Enter right branch angle: "))
    starting_branch_length = float(input("Enter starting branch length: "))
    recursion_depth = int(input("Enter recursion depth: "))
    reduction_factor = int(input("Enter branch length reduction percent : "))
    
  
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.left(90)  # Point the turtle upwards
    t.color("brown")
    t.speed(0)  
    t.penup()
    t.goto(0, -200)  # Start at the bottom of the screen
    t.pendown()

    draw_tree(t, starting_branch_length, left_angle, right_angle, recursion_depth, reduction_factor/100) 
    t.hideturtle()    
    screen.exitonclick()
   

if __name__ == "__main__":
    main()
