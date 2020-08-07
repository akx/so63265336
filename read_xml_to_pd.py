import xml.sax
import pandas as pd

from util import start_memory_usage_thread


class BadgeHandler(xml.sax.ContentHandler):
    def __init__(self, rows):
        self.rows = rows

    def startElement(self, tag, attributes):
        if tag == "row":
            self.rows.append(dict(attributes.items()))


t, stop_event = start_memory_usage_thread()
try:
    rows = []
    handler = BadgeHandler(rows)
    xml.sax.parse("badges.xml", handler)
    print("Finished XML")
    df = pd.DataFrame(rows)
finally:
    stop_event.set()
