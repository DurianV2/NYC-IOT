from information_handler import information_handler_
from request_handler import request_handler_
from background_sync import background_sync_
from controller import controller_
import threading
import time

class server_:

    def __init__(self):
        self.information_handler = information_handler_()
        self.request_handler = request_handler_()
        self.controller = controller_()
        self.sync_time = time.time()
        self.has_background_caller = False
        thread = threading.Thread(target=self.controller.buttonwrapper.wait_for_press, args=())
        self.thread = thread
        self.event = thread.Event()
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def main(self):
        while(True):
            if(self.event.is_set()):
                if(not self.controller.led_status_ok):
                    self.controller.led_status_ok = True
                    self.event.clear()
            if(not self.information_handler.is_home and not self.has_background_caller):
                background_caller = background_sync_()
                self.has_background_caller = True
                if(self.controller.led_status_ok):
                    self.controller.ledwrapper.set_red(True)
            else:
                if(self.has_background_caller):
                    if(background_caller.is_home):
                        background_caller.end()
                        self.has_background_caller = False
                        controller.oledwrapper.clear_screen()
                        self.information_handler.reset()
                        self.controller.oled_set = False
                        if(not self.controller.led_status_ok):
                            self.controller.ledwrapper.set_green(True)
            if(self.information_handler.first_warning and not self.controller.oled_set):
                controller.oledwrapper.display_text("Where are you?")
                self.controller.oled_set = True
                break
        if(self.has_background_caller):
            background_caller.end()

server = server_()
server.main()
