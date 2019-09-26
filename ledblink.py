import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

i = 0
while True:
    i = i + 1
    GPIO.output(8, True)
    time.sleep(0.5)
    GPIO.output(8, False)
    time.sleep(0.5)
    if i == 5:
 	break;
