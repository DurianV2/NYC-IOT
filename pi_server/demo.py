import pygame
from time import sleep
from utils import sms
from output_wrappers.buttonwrapper import ButtonWrapper as btn
from output_wrappers.ledwrapper import LedWrapper as led
from output_wrappers.oledwrapper import OledWrapper as oled

def play_sound(location):
	pygame.mixer.init()
 	pygame.mixer.music.load(location)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
    		continue

start_button = btn(26)
start_button.wait_for_press(None)
screen = oled("Let's do this")
sleep(2)

screen.display_text("Doing the LED")

status_led = led(16, 20)
status_led.set_green(True)
sleep(5)
status_led.set_green(False)
status_led.set_red(True)
play_sound("audio/first.mp3")

sleep(5)
play_sound("audio/second.mp3")
screen.display_text("Sending texts to your friends")
text_messages = sms.SMS("Help me!")
for i in range(5):
    screen.display_text(str("Sending "+ str(i) + " message"))
    text_messages.send_text()
    sleep(2)

play_sound("audio/third.mp3")
screen.display_text("Signaling the Batman")
text_messages = sms.SMS("Batman & Robin, we need you. Please help our person.")
text_messages.send_text()
