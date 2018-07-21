import bluetooth
from time import sleep

class BluetoothWrapper:
    check_timeout = None
    def __init__(self, timeout=5):
        self.check_timeout=timeout
    def check_for_person(self, address):
        for i in range(5):
            result = bluetooth.lookup_name(address, self.check_timeout)
            if (result is not None):
                return result
        return None
