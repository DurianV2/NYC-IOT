import threading
import time
from request_handler import request_handler_

class background_sync_(object):

    def __init__(self, interval=1, sync_url=None):
        self.is_home = False
        self.interval = interval
        self.stop = True
        self.request_handler = request_handler_()
        self.sync_url = sync_url
        stop_event = threading.Event()
        self.stop_event = stop_event
        thread = threading.Thread(target=self.run, args=(stop_event,))
        self.thread = thread
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self, stop_event):
        start_time = time.time()
        while not stop_event.is_set():
            if(time.time() - start_time >= 1 and self.sync_url is not None):
                json = self.request_handler.get_sync(self.sync_url)
                                # if(!json.is_home or !json.first_trigger):
                                #     self.is_home = True
                                #     self.end()
                                #     return json
                start_time = time.time()
            # else:
            #     # print("something is none")
            #     start_time = time.time()

    def end(self):
        self.stop_event.set()
        # self.stop = True
        # self.thread.join()

example = background_sync_(sync_url = "http://honeyimhome-210903.appspot.com")
current_time = time.time()
while True:
    if(time.time() - current_time >= 1):
        print("ending")
        # stop_event.set
        example.end()
        break

print("done")
# while True:
#     print("no")
#     time.sleep(1)
# time.sleep(3)
# print('Checkpoint')
# time.sleep(2)
# print('Bye')
