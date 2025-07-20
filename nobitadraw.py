from turtle import *

def spen(x,y):
	penup()
	goto(x,y)
	pendown()

spen(0,0)
for i in range(100):
	fd(11)
	lt(7)
	fd(1)


done()
