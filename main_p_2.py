import RPi.GPIO as GPIO
from time import sleep
from turtle import *
import time
#import numpy as np
import sys
#import motor
from ultrasound import *
import os
import logging
from time import gmtime, strftime


timestamp=strftime("%Y-%m-%d %H:%M:%S", gmtime())
logname='bot_'+timestamp
logging.basicConfig(filename=logname,level=logging.DEBUG)

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
	print "Front distance:" + str(frontsonar) + ", Left distance:"+ str(leftsonar) + ", Right distance:" + str(rightsonar)
	if (frontsonar > 15):
		#motor_forward()
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
	logging.info('strftime("%Y-%m-%d %H:%M:%S", gmtime())'+'Forward'+'(front dist:' + str(frontsonar) + 'left dist:' + str(leftsonar) + 'right dist:' + str(rightsonar)+')')
	# Yaha par sonar ka left, right and front value print hoga 

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
    logging.info('strftime("%Y-%m-%d %H:%M:%S", gmtime())' + 'back' + '15 cm') #Yaha par standard distance print kar back dabana par kitna back jata hai zameen par uska kitna hai usko scale down kar yaha par print kar kyunki back me apna koi sonar ni hai 


def left():
	motor_left()
	tc.left(90)
	tl.left(90)
	tr.left(90)
	logging.info('strftime("%Y-%m-%d %H:%M:%S", gmtime())' + 'Left'+'(front dist:' + str(frontsonar) + 'left dist:' + str(leftsonar) + 'right dist:' + str(rightsonar)+')')

def right():
	motor_right()
	tc.right(90)
	tl.right(90)
	tr.right(90)
	logging.info('strftime("%Y-%m-%d %H:%M:%S", gmtime())' + 'Right'+'(front dist:' + str(frontsonar) + 'left dist:' + str(leftsonar) + 'right dist:' + str(rightsonar)+')')



def map2d():
	ts = move.getscreen()
	ts.getcanvas().postscript(file='turtle.eps', colormode='color')
	os.system("cp logname.log /opt/lamp/project/")
	os.system("cp turtle.eps /opt/lamp/project")
	os.system("chmod 777 -R /opt/lamp/project")# Yeh command mujhe doubt hai chalega kyunki uske lie tere ko root hona padega. Try karke dekh ni challa to thoda net par dekh lena even pehle wale bhi opt me copy tabhi hota hai jab root ho aise copy ni hota hai woh .


def bot_scan():
	global frontsonar,leftsonar,rightsonar
	frontsonar = distance_cm(8,7)
	leftsonar  = distance_cm(8,31)
	rightsonar = distance_cm(8,29)
	
onkey(forward, "Up")
onkey(left, "Left")
onkey(right, "Right")
onkey(down, "Down")
onkey(map2d, 'p')

listen()
mainloop()



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