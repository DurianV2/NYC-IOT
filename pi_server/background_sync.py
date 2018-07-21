import threading
import time
from request_handler import request_handler_

class background_sync_(object):

    def __init__(self, interval=1, sync_url=None):
        self.is_home = False
        self.first_warning = False
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
                json_ = self.request_handler.get_sync(self.sync_url)
                # self.is_home = json_["is_home"]
                # self.first_warning = json_["send_alert"]
                self.is_home = True
                self.first_warning = False
                if(self.is_home and not self.first_warning):
                    self.end()
                    return json_
                start_time = time.time()
            # else:
            #     # print("something is none")
            #     start_time = time.time()

    def end(self):
        self.stop_event.set()
        # self.stop = True
        # self.thread.join()

example = background_sync_(sync_url = "http://honeyimhome-210903.appspot.com/sync")
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
