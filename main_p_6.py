import RPi.GPIO as GPIO
from time import sleep
from turtle import *
import time
#import numpy as np
import sys
from motor import *
from ultrasound import *
from PIL import Image
import os
import logging
import socket
import fcntl
import struct
from time import gmtime, strftime

os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()
timestamp=strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
logname='bot_'+timestamp+'.log'
logging.basicConfig(filename=logname,level=logging.DEBUG)

setup(640, 640)
Screen()
title("2D Mapgen")
tc = Turtle()
tl = Turtle()
tr = Turtle()
tf = Turtle()

tc.showturtle()
tl.hideturtle()
tr.hideturtle()
tf.hideturtle()

tc.left(90)
tl.left(90)
tr.left(90)
tf.left(90)

tracer(1, 0)


leftsonar,rightsonar,frontsonar=0,0,0

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,  # SIOCGIFADDR
		struct.pack('256s', ifname[:15])
	)[20:24])

def border_left():
	tl.pendown()
	tl.color("black", "black")
	tl.begin_fill()
	tl.circle(1)
	tl.end_fill()

def border_right():
	tr.pendown()
	tr.color("black", "black")
	tr.begin_fill()
	tr.circle(1)
	tr.end_fill()

def border_front():
	tf.pendown()
	tf.color("black", "black")
	tf.begin_fill()
	tf.circle(1)
	tf.end_fill()


def forward():
	bot_scan()
	print "Front distance:" + str(frontsonar) + ", Left distance:"+ str(leftsonar) + ", Right distance:" + str(rightsonar)
	if (frontsonar > 15):
		motor_forward()
		tc.forward(15)
	    	a,b=tc.pos()
	    	a,b= int(a), int(b)
		""""if(tc.heading() == 90.0):
			if leftsonar<50:
				tl.penup()
				tl.setpos(a-leftsonar,b)
				border_left()
			if rightsonar<50:
				tr.penup()
				tr.setpos(a+rightsonar,b)
				border_right()

			if(tc.heading() == 270.0):
			if leftsonar<50:
				tl.penup()
				tl.setpos(a+leftsonar,b)
				border_left()
			if rightsonar<50:
				tr.penup()
				tr.setpos(a-rightsonar,b)
				border_right()	
			if(tc.heading() == 0.0):
				if leftsonar<50:
					tl.penup()
					tl.setpos(a,b+leftsonar)
					border_left()
				if rightsonar<50:
					tr.penup()
					tr.setpos(a,b-rightsonar)
					border_right()
			if( tc.heading() == 180.0):
				if leftsonar<50:
					tl.penup()
					tl.setpos(a,b-leftsonar)
					border_left()
				if rightsonar<50:
					tr.penup()
					tr.setpos(a,b+rightsonar)
					border_right()



				"""
	else:
		a,b = tc.pos()
		if tc.heading() == 90.0:
			tf.penup()
			tf.setpos(a,b+frontsonar)
			border_front()

			if leftsonar<50:
				tl.penup()
				tl.setpos(a-leftsonar,b)
				border_left()
			if rightsonar<50:
				tr.setpos(a+rightsonar,b)
				tr.penup()
				border_right()

		if tc.heading() == 270.0:
			tf.penup()
			tf.setpos(a,b-frontsonar)
			border_front()

			if leftsonar<50:
				tl.penup()
				tl.setpos(a-leftsonar,b)
				border_left()
			if rightsonar<50:
				tr.setpos(a+rightsonar,b)
				tr.penup()
				border_right()

		if tc.heading() == 0.0:
			tf.penup()
			tf.setpos(a+frontsonar,b)
			border_front()

			if leftsonar<50:
				tl.penup()
				tl.setpos(a,b+leftsonar)
				border_left()
			if rightsonar<50:
				tr.penup()
				tr.setpos(a,b-rightsonar)
				border_right()

		if tc.heading() == 180.0:
			tf.penup()
			tf.setpos(a-frontsonar,b)
			border_front()

			if leftsonar<50:
				tl.penup()
				tl.setpos(a,b+leftsonar)
				border_left()
			if rightsonar<50:
				tr.penup()
				tr.setpos(a,b-rightsonar)
				border_right()
		
			
	#print int(a),int(b)
	logging.info(strftime("%Y-%m-%d %H:%M:%S", time.localtime())+',Forward'+'(front dist:' + str(frontsonar) + ',Left dist:' + str(leftsonar) + ',Right dist:' + str(rightsonar)+')')
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
	logging.info(strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'Back' + '15 cm') #Yaha par standard distance print kar back dabana par kitna back jata hai zameen par uska kitna hai usko scale down kar yaha par print kar kyunki back me apna koi sonar ni hai 


def left():
	motor_left()
	tc.left(90)
	tl.left(90)
	tr.left(90)
	logging.info(strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ',Left'+'(front dist:' + str(frontsonar) + ',Left dist:' + str(leftsonar) + ',Right dist:' + str(rightsonar)+')')

def right():
	motor_right()
	tc.right(90)
	tl.right(90)
	tr.right(90)
	logging.info(strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ',Front'+'(front dist:' + str(frontsonar) + ',Left dist:' + str(leftsonar) + ',Right dist:' + str(rightsonar)+')')



def map2d():
	ts = tc.getscreen()
	ts.getcanvas().postscript(file='map_'+ timestamp +'.eps', colormode='color')
	img = Image.open('map_'+ timestamp +'.eps')
	img.save('map_' + timestamp + '.png', "png")
	os.remove('map_'+ timestamp +'.eps')
	os.system("cp "+ logname  +" /var/www/map_images/")
	os.system("cp map_"+ timestamp +".png /var/www/map_images/")
	print "http://" + get_ip_address('wlan0') + '/map_images/' + logname
	print "http://" + get_ip_address('wlan0') + '/map_images/map_' + timestamp + '.png' 


def bot_scan():
	global frontsonar,leftsonar,rightsonar
	sensor_values_front = list()
	sensor_values_left = list()
	sensor_values_right = list()
	for x in range(0,10):
		val = distance_cm(8,7)
		sensor_values_front.append(val)
		val = distance_cm(8,31)
		sensor_values_left.append(val)
		val = distance_cm(8,29)
		sensor_values_right.append(val)
		
	frontsonar = sum(sensor_values_front)/float(len(sensor_values_front))
	leftsonar  = sum(sensor_values_left)/float(len(sensor_values_left))
	rightsonar = sum(sensor_values_right)/float(len(sensor_values_right))
	
onkey(forward, "Up")
onkey(left, "Left")
onkey(right, "Right")
onkey(down, "Down")
onkey(map2d, 'p')

listen()
mainloop()