import turtle as T
import canvasvg
from PIL import Image
import os
T.setup(640, 640)
T.Screen()
T.title("Turtle Keys")
move = T.Turtle()
T.showturtle()

def forward():
    move.forward(15)

def left():
    move.left(90)

def right():
    move.right(90)

def down():
    move.back(15)

def map2d():
	canvasvg.saveall("image.svg", move.getscreen().getcanvas())
	ts = move.getscreen()
	ts.getcanvas().postscript(file='turtle.eps', colormode='color')
	img = Image.open("turtle.eps")
	img.save("test.png", "png")
	os.remove("turtle.eps")

T.onkey(forward, "Up")
T.onkey(left, "Left")
T.onkey(right, "Right")
T.onkey(down, "Down")
T.onkey(map2d, 'p')
T.listen()
T.mainloop()