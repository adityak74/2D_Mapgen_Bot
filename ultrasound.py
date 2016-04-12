# Module: ultrasound.py
# This module can be used to operate an HC-SR04 ultrasonic sensor
# from a raspberry pi GPIO.

# setup which pins are which
TRIG = 8
ECHO = 7

# set the trigger pulse length and timeouts
pulsetrigger = 0.0001 # Trigger duration in seconds
timeout = 100        # Length of sm timeout
measuretimes = 3
sleeptime = 0.001

timeout = timeout*(1000/57/2)
print timeout

def configure(trigger, echo):
    TRIG = trigger
    ECHO = echo
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def fire_trigger():
    # Set trigger high for 0.0001s then drop it low
    GPIO.output(TRIG, True)
    time.sleep(pulsetrigger)
    GPIO.output(TRIG, False)

def wait_for_echo(desired_state):
    countdown = timeout
    while (GPIO.input(ECHO) != desired_state and countdown > 0):
        countdown = countdown - 1
    return (countdown > 0) # Return true if success, false if timeout

def measure_time():
    # Fire the trigger to set the whole thing in motion
    fire_trigger()

    # Check that the echo goes high....
    if wait_for_echo(1):
        # Start the timer and wait for the echo to go low
        echo_start = time.time()
        if wait_for_echo(0):
            # Stop the timer
            echo_end = time.time()
            return echo_end - echo_start
        else:
            # print "Timeout 2"
            return -1
    else:
        # print "Timeout 1"
        return -1
    
def measure_average_time():
    count = 1
    total_time = 0
    while(count <= measuretimes):
        total_time = total_time + measure_time()
        time.sleep(0.01)
        count = count + 1
    return total_time / measuretimes
        
def distance_cm():
    configure(TRIG, ECHO)
    time = measure_average_time()
    if time < 0:
        return -1
    else:
        return time * (1000000 / 58)


# if __name__ == "__main__":
#     print "Starting ultrasound"
#     # Set up the GPIO board
#     GPIO.setmode(GPIO.BOARD)

#     # Tell the Pi which pins the ultrasound is on
#     configure(TRIG, ECHO)

#     try:
#         while True:
#             distance = distance_cm()
#             if distance < 0:
#                 tm = 0 # print "Timeout"
#             else:
# 		val = ""
# 		space = "-"
# 		disanceround = (int(round(distance)))
# 		for num in range(0,disanceround):
# 			val += space
# 		#print val
# 		print ("%.0f cm " % (int(round(distance))))+val+">"
#             time.sleep(sleeptime)

#     except KeyboardInterrupt:
#         print "Stopping"
#         GPIO.cleanup()

