import turtle

# Create a turtle object
pen = turtle.Turtle()

# Move to a desired location (optional)
pen.penup()
pen.goto(-200, 0)  # (x, y) coordinates
pen.pendown()

# Write text
pen.write("Hello, Turtle!", font=("Arial", 24, "normal"))

# Hide the turtle (optional)


# Keep the window open
turtle.done()