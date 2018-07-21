import RPi.GPIO as GPIO
from output_wrappers.ledwrapper import LedWrapper
from output_wrappers.oledwrapper import OledWrapper
from output_wrappers.buttonwrapper import ButtonWrapper

class controller_:

    def __init__(self):
        self.ledwrapper = LedWrapper(16, 20)
        self.oledwrapper = OledWrapper("yello")
        self.buttonwrapper = ButtonWrapper(23)
        self.oled_set = False
        self.led_status_ok = True
