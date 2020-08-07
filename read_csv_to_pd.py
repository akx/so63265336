import gc
import time

import pandas as pd

from util import start_memory_usage_thread

t, stop_event = start_memory_usage_thread()
try:
    df = pd.read_csv("badges.csv", header=0, parse_dates=["Date"], memory_map=True)
    print(df.head())
    gc.collect()
    time.sleep(1)
finally:
    stop_event.set()
