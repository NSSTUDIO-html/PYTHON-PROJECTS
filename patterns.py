import turtle

star = turtle.Turtle()
star.speed(10)
star.penup()
star.goto(-200,0)
star.pendown()
for i in range(5):
    star.forward(400)
    star.right(144)  # 144 degrees creates a 5-pointed star

turtle.done()