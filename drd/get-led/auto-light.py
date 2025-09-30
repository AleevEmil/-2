import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
button = 6
state = 0
GPIO.setup(button, GPIO.IN)
while True:
    GPIO.output(led, not (GPIO.input(button)))
    time.sleep(0.5)
