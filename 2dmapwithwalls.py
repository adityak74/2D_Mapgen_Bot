from turtle import *
setup(640, 640)
Screen()
title("Turtle Keys")
tc = Turtle()
tl = Turtle()
tr = Turtle()

tc.showturtle()
tl.hideturtle()
tr.hideturtle()

tc.left(90)
tl.left(90)
tr.left(90)

tracer(1, 0)

def border():
	tl.pendown()
	tr.pendown()
	tl.color("black", "black")
	tl.begin_fill()
	tl.circle(1)
	tl.end_fill()

	tr.color("black", "black")
	tr.begin_fill()
	tr.circle(1)
	tr.end_fill()


def forward():
    tc.forward(15)
    a,b=tc.pos()
    a,b= int(a), int(b)
    if(tc.heading() == 90.0 or tc.heading() == 270.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a-10,b)
    	tr.setpos(a+10,b)
    	border()
    if(tc.heading() == 0.0 or tc.heading() == 180.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a,b-10)
    	tr.setpos(a,b+10)
    	border()
    #print int(a),int(b)

def down():
    tc.back(15)
    a,b=tc.pos()
    a,b= int(a), int(b)
    if(tc.heading() == 90.0 or tc.heading() == 270.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a-10,b)
    	tr.setpos(a+10,b)
    	border()
    if(tc.heading() == 0.0 or tc.heading() == 180.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a,b-10)
    	tr.setpos(a,b+10)
    	border()
    #print int(a),int(b)

def left():
    tc.left(90)
    tl.left(90)
    tr.left(90)

def right():
    tc.right(90)
    tl.right(90)
    tr.right(90)


def map2d():
	ts = move.getscreen()
	ts.getcanvas().postscript(file='turtle.eps', colormode='color')

onkey(forward, "Up")
onkey(left, "Left")
onkey(right, "Right")
onkey(down, "Down")
onkey(map2d, 'p')
listen()
mainloop()