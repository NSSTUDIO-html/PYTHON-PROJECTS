import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create turtle
tree = turtle.Turtle()
tree.hideturtle()
tree.speed("fastest")
tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()

# Draw a branch
def draw_branch(branch_length, t):
    if branch_length > 10:
        # Set branch thickness
        t.pensize(branch_length / 10)

        # Set color to brown for branches
        t.color("saddlebrown")
        t.forward(branch_length)

        # Right branch
        angle = random.randint(15, 30)
        t.right(angle)
        draw_branch(branch_length - random.randint(10, 15), t)

        # Left branch
        t.left(angle * 2)
        draw_branch(branch_length - random.randint(10, 15), t)

        # Restore orientation and position
        t.right(angle)
        t.backward(branch_length)
    else:
        # Draw a leaf
        t.color("forestgreen")
        t.begin_fill()
        t.circle(3)
        t.end_fill()

# Start drawing
draw_branch(100, tree)

# Keep window open
screen.mainloop()