from turtle import *
speed(30)
shape("turtle")
def spen(x,y):
	penup()
	goto(x,y)
	pendown()
	
	
spen(200,-20)
color("orange")
bgcolor("black")
for _ in range(100):
	left(90)
	for _ in range(2):
		fd(200)
		lt(1)
		rt(15)
		back(100)
		lt(15)
		

done()