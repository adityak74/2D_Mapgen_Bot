import RPi.GPIO as GPIO
from time import sleep
from turtle import *
import time
import numpy as np
import cv2
import sys
import motor
import ultrasound
import camera

setup(640, 640)
Screen()
title("2D Mapgen")
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


def forward(offseta,offsetb):
    tc.forward(15)
    a,b=tc.pos()
    a,b= int(a), int(b)
    if(tc.heading() == 90.0 or tc.heading() == 270.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a-offseta,b)
    	tr.setpos(a+offsetb,b)
    	border()
    if(tc.heading() == 0.0 or tc.heading() == 180.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a,b-offseta)
    	tr.setpos(a,b+offsetb)
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

def bot_scan():
	front_free = 0
	left_free = 0
	right_free = 0 
	front_dist = distance_cm()
	if front_dist < 0:
		front_free = 1
	else :
		front_free = 0
	motor_left()
	left_dist = distance_cm()
	if left_dist < 0:
		left_free = 1
	else :
		left_free = 0
	motor_left_back()
	motor_right()
	right_dist = distance_cm()
	if right_dist < 0:
		right_free = 1
	else :
		right_free = 0
	motor_right_back()

	if front_free:
		bot_scan()
	elif front_dist >= 10:
		bot_scan()
	else:
		motors_stop()
		if left_free:
			motor_left()
		elif right_free:
			motor_right()
		else:
			motors_stop()
			print "Blocked. Cannot move further"




onkey(forward, "Up")
onkey(left, "Left")
onkey(right, "Right")
onkey(down, "Down")
onkey(map2d, 'p')
listen()
mainloop()