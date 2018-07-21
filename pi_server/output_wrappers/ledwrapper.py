import RPi.GPIO as GPIO

class LedWrapper:

    green_pin = None
    red_pin = None

    def __init__(self, green_pin, red_pin):
        GPIO.setmode(GPIO.BCM)
        self.green_pin = green_pin
        self.red_pin = red_pin

    def set_green(self, turningOn):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.output(self.green_pin, not turningOn)

    def set_red(self, turningOn):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.output(self.red_pin, not turningOn)
