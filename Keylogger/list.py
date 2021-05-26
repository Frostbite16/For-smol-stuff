# import the time module
import time


while True:
    print("OI")
    mins, secs = divmod(0, 1)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    t = -1