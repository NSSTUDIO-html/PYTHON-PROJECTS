import turtle
import random

def colorful_spiral(num_circles=50, radius_increment=5, angle_increment=10):
    """Draws a colorful spiral of circles."""
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")  # Dark background for vibrant colors
    t.speed(0)
    t.hideturtle()

    radius = 10
    angle = 0

    for _ in range(num_circles):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(angle)
        t.forward(radius)
        t.left(90)
        t.color(random.random(), random.random(), random.random())  # Random color
        t.circle(radius / 2)
        radius += radius_increment
        angle += angle_increment

    screen.exitonclick()

def colorful_polygons(num_polygons=20, max_size=150):
    """Draws a series of colorful polygons."""
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("lightgray")
    t.speed(0)
    t.hideturtle()

    for _ in range(num_polygons):
        sides = random.randint(3, 8)  # Random number of sides (triangle to octagon)
        size = random.randint(50, max_size)
        x = random.randint(-screen.window_width() // 2 + max_size, screen.window_width() // 2 - max_size)
        y = random.randint(-screen.window_height() // 2 + max_size, screen.window_height() // 2 - max_size)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(random.random(), random.random(), random.random())
        t.begin_fill()
        for _ in range(sides):
            t.forward(size)
            t.left(360 / sides)
        t.end_fill()

    screen.exitonclick()

def colorful_circles_pattern(num_circles=36, radius=100):
    """Draws a circular pattern with colorful circles."""
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")
    t.speed(0)
    t.hideturtle()

    for _ in range(num_circles):
        angle = (360 / num_circles) * _
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(angle)
        t.forward(radius)
        t.color(random.random(), random.random(), random.random())
        t.dot(radius / 3) #draws a filled circle.

    screen.exitonclick()

def colorful_starburst(num_rays=20, ray_length=200):
  """Draws a colorful starburst pattern."""
  t = turtle.Turtle()
  screen = turtle.Screen()
  screen.bgcolor("black")
  t.speed(0)
  t.hideturtle()

  for _ in range(num_rays):
    angle = (360 / num_rays) * _
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(angle)
    t.color(random.random(), random.random(), random.random())
    t.forward(ray_length)

  screen.exitonclick()

# Example usage:
colorful_spiral()
colorful_polygons()
colorful_circles_pattern()
colorful_starburst()
