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

tc.showturtle()
tl.hideturtle()
tr.hideturtle()

tc.left(90)
tl.left(90)
tr.left(90)

tracer(1, 0)


leftsonar,rightsonar,frontsonar=0,0,0

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,  # SIOCGIFADDR
		struct.pack('256s', ifname[:15])
	)[20:24])

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
	os.system("cp "+ logname  +" /var/www/map_images/")
	os.system("cp map_"+ timestamp +".eps /var/www/map_images/")
	print "http://" + get_ip_address('wlan0') + '/map_images/' + logname
	print "http://" + get_ip_address('wlan0') + '/map_images/map_' + timestamp + '.eps' 


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
