from information_handler import information_handler_
from request_handler import request_handler_
from background_sync import background_sync_
import time

class server_:

    def __init__(self):
        self.information_handler = information_handler_()
        self.request_handler = request_handler_()
        self.sync_time = time.time()

    def main(self):
        while(True):
            if(not(self.information_handler.is_home)):
                background_caller = background_sync_()
            else:
                background_caller.end()
                break
