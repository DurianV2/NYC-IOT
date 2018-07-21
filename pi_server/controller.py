import RPi.GPIO as GPIO
from output_wrappers.ledwrapper import LedWrapper
from output_wrappers.oledwrapper import OledWrapper

class controller_:

    def __init__(self):
        self.ledwrapper = LedWrapper(16, 20)
        self.oledwrapper = OledWrapper("yello")
        self.oled_set = False
        self.led_status_ok = True
