from turtle import *

penup()
goto(0,0)
pendown()
color("blue")
begin_fill()
for _ in range(40):
	
	left(10)
	forward(30)
end_fill()
penup()
goto(-110,20)
pendown()
color("red")
begin_fill()
right(40)
forward(200)
right(90)
forward(50)
right(90)
forward(200)
right(90)
forward(50)
end_fill()
done()