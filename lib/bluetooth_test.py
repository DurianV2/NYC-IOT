import bluetooth
import time

while True:
    result = bluetooth.lookup_name("10:f1:f2:f1:2d:59", timeout=5)

    if (result is not None):
        print("Innocent is home")
    else:
        print("Innoncent is not home")

    time.sleep(1)
