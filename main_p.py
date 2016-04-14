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


leftsonar,rightsonar,frontsonar=0,0,0

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
	bot_scan()
	print "Front distance:" + string(frontsonar) + "Left distance:"+ str(leftsonar) + "Right distance:" + str(rightsonar)
	if (frontsonar > 15):
		motor_forward()
		tc.forward(15)
	    a,b=tc.pos()
	    a,b= int(a), int(b)
	    if(tc.heading() == 90.0 or tc.heading() == 270.0):
	    	tl.penup()
	    	tr.penup()
	    	tl.setpos(a-leftsonar,b)
	    	tr.setpos(a+rightsonar,b)
	    	border()
	    if(tc.heading() == 0.0 or tc.heading() == 180.0):
	    	tl.penup()
	    	tr.penup()
	    	tl.setpos(a,b-leftsonar)
	    	tr.setpos(a,b+rightsonar)
	    	border()
	    #print int(a),int(b)

def down():
	motor_back()
    tc.back(15)
    a,b=tc.pos()
    a,b= int(a), int(b)
    if(tc.heading() == 90.0 or tc.heading() == 270.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a-leftsonar,b)
    	tr.setpos(a+rightsonar,b)
    	border()
    if(tc.heading() == 0.0 or tc.heading() == 180.0):
    	tl.penup()
    	tr.penup()
    	tl.setpos(a,b-leftsonar)
    	tr.setpos(a,b+rightsonar)
    	border()
    #print int(a),int(b)

def left():
	motor_left()
    tc.left(90)
    tl.left(90)
    tr.left(90)

def right():
	motor_right()
    tc.right(90)
    tl.right(90)
    tr.right(90)


def map2d():
	ts = move.getscreen()
	ts.getcanvas().postscript(file='turtle.eps', colormode='color')

"""def bot_scan():
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
"""

def bot_scan():
	global frontsonar,leftsonar,rightsonar
	frontsonar = distance_cm(8,7)
	leftsonar  = distance_cm(8,29)
	rightsonar = distance_cm(8,31)
	
onkey(forward, "Up")
onkey(left, "Left")
onkey(right, "Right")
onkey(down, "Down")
onkey(map2d, 'p')

listen()
mainloop()