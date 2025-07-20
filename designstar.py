from turtle import *
speed(20)
color("blue")
pensize(5)
for _ in range(10):
	left(90)
	for _ in range(10):
		forward(100)
		left(90)
		fd(100)
		rt(180)
		fd(100)
		rt(90)
		fd(100)
		lt(2)

done()