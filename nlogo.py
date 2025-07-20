from turtle import *

pensize(10)
speed(10)
def spen(x,y):
	penup()
	goto(x,y)
	pendown()
	
spen(0,0)
for _ in range(10):
	right(-25)
	forward(10)


hideturtle()
done()