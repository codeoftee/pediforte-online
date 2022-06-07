
import time


def get_time(readable=False):
    if readable:
        r = time.ctime()
        return r
    millis = int(round(time.time() * 1000))
    return millis
