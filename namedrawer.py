import tkinter as tk
import turtle

class TurtleApp:
    def __init__(self, master):
        self.master = master
        master.title("Turtle Graphics App")

        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.turtle_screen = turtle.TurtleScreen(self.canvas)
        self.pen = turtle.RawTurtle(self.turtle_screen)
        self.pen.speed(5)
        self.pen.shape("turtle")
        self.pen.hideturtle()  # Hide the default turtle arrow

        self.draw_button = tk.Button(master, text="Draw Shapes", command=self.draw_shapes)
        self.draw_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_canvas)
        self.reset_button.pack(pady=5)

    def spen(self, x, y):
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()

    def draw_shapes(self):
        self.pen.pensize(5)

        # First shape
        self.spen(-250, 0)
        self.pen.left(90)
        self.pen.forward(100)
        self.pen.right(140)
        self.pen.forward(130)
        self.pen.left(140)
        self.pen.forward(100)

        # Second shape
        self.spen(-100, 0)
        self.pen.color("red")
        self.pen.left(-25)
        self.pen.forward(100)
        self.pen.right(125)
        self.pen.forward(100)

        # Third shape
        self.spen(150, 90)
        self.pen.color("green")
        self.pen.left(60)
        self.pen.back(100)
        self.pen.right(90)
        self.pen.forward(85)
        self.pen.left(90)
        self.pen.forward(60)
        self.pen.left(90)
        self.pen.forward(30)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(30)

        # Fourth shape
        self.spen(230, 0)
        self.pen.color("cyan")
        self.pen.left(180)
        self.pen.left(-25)
        self.pen.forward(100)
        self.pen.right(125)
        self.pen.forward(100)

        # Fifth shape
        self.spen(0, -100)
        self.pen.color("gold")
        self.pen.right(120)
        self.pen.forward(100)
        self.pen.left(90)
        self.pen.forward(50)
        self.pen.left(90)
        self.pen.forward(100)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(100)

    def reset_canvas(self):
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.pendown()
        self.pen.setheading(0)  # Reset orientation

if __name__ == "__main__":
    root = tk.Tk()
    app = TurtleApp(root)
    root.mainloop()
