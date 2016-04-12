import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

#Motor1 - Left
#Motor2 - Right

Motor1A = 16
Motor1B = 18
Motor1E = 12

Motor2A = 13
Motor2B = 15
Motor2E = 33

def motors_setup():
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)

def motors_stop():
	motors_setup()
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)

def motor_forward():
	motors_setup() 

	print "Turning motors on"

	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(2)
	 
	print "Stopping motors"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	 
	GPIO.cleanup()

def motor_right():
	motors_setup()
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	sleep(2)
	GPIO.output(Motor1E,GPIO.LOW)

def motor_right_back():
	motors_setup()
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	sleep(2)
	GPIO.output(Motor1E,GPIO.LOW)

def motor_left():
	motors_setup()
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	sleep(2)
	GPIO.output(Motor2E,GPIO.LOW)

def motor_left_back():
	motors_setup()
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	sleep(2)
	GPIO.output(Motor2E,GPIO.LOW)

def motor_back():
	motors_setup()
	print "Turning motors on"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(2)
	 
	print "Stopping motors"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	 
	GPIO.cleanup()