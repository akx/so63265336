import datetime
import os
import threading
import time

import psutil


def get_memory_usage_kb():
    return int(psutil.Process(os.getpid()).memory_info().rss / 1024)


def start_memory_usage_thread():
    event = threading.Event()

    def dump(t0, prefix=""):
        print(
            f"{prefix}"
            f"{datetime.datetime.now().isoformat():25s} "
            f"{time.time() - t0:>15.2f} "
            f"{get_memory_usage_kb():10d}k"
        )

    def loop():
        t0 = time.time()
        while not event.wait(0.5):
            dump(t0)
        time.sleep(1)
        dump(t0, prefix="Final:")

    thread = threading.Thread(target=loop)
    thread.start()
    return (thread, event)
