from time import sleep
from utils import sms
from output_wrappers.buttonwrapper import ButtonWrapper as btn
from output_wrappers.ledwrapper import LedWrapper as led
from output_wrappers.oledwrapper import OledWrapper as oled

start_button = btn(26)
start_button.wait_for_press()
print("let's do this")

screen = oled("Let's do this")
sleep(2)

screen.display_text("Doing the LED")

status_led = led(16, 20)
status_led.set_green(True)
sleep(5)
status_led.set_green(False)
status_led.set_red(True)

sleep(10)
screen.display_text("Sending texts to your friends")
text_messages = sms.SMS("Help me!")
for i in range(5):
    print("Sending ", i, "message")
    text_messages.send_text()
    sleep(2)

screen.display_text("Signaling the Batman")
text_messages = sms.SMS("Batman & Robin, we need you. Please help our person.")
text_messages.send_text()
