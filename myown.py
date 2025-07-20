from turtle import *
speed(5)
bgcolor("black")
penup()
goto(0,0)
pendown()
for _ in range(11):
	for colors in ["red","orange","yellow",			"white" ,"cyan","blue" ]:
		goto(0,0)
		color(colors)
	
		for _ in range(1):
			forward(100)
			left(5)
			forward(100)
			left(-15)
			
		
done()