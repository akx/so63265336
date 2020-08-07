import xml.sax

import pandas as pd

from util import start_memory_usage_thread


class BadgeHandler(xml.sax.ContentHandler):
    def __init__(self, rows):
        self.rows = rows

    def startElement(self, tag, attributes):
        if tag == "row":
            self.rows.append(dict(attributes.items()))


def read_rows():
    rows = []
    handler = BadgeHandler(rows)
    xml.sax.parse("badges.xml", handler)
    print("Finished XML")
    return rows


def make_df(rows):
    print("Making DF...")
    df = pd.DataFrame(rows)
    print("Cleaning up rows...")
    rows[:] = []
    print("Coercing date...")
    df["Date"] = pd.to_datetime(df["Date"])
    print("Completing...")
    return df


t, stop_event = start_memory_usage_thread()
try:
    df = make_df(read_rows())
finally:
    stop_event.set()
