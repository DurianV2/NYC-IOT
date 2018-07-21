import RPi.GPIO as GPIO
import time

class ButtonWrapper:

    pin = None

    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin

    def wait_for_press(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        while True:
            input_state = GPIO.input(self.pin)
            if input_state == False:
                break
