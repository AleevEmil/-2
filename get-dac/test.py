import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_bits, GPIO.OUT)
GPIO.output(dac_bits, 0)