import csv
import xml.sax

from util import start_memory_usage_thread


class BadgeHandler(xml.sax.ContentHandler):
    def __init__(self, output_file):
        self.output_file = output_file
        self.writer = None

    def startElement(self, tag, attributes):
        if tag == "row":
            if self.writer is None:
                self.writer = csv.DictWriter(
                    self.output_file, list(attributes.keys()), extrasaction="ignore"
                )
                self.writer.writeheader()
            self.writer.writerow(dict(attributes.items()))


t, stop_event = start_memory_usage_thread()
try:
    with open("badges.csv", "w") as outf:
        handler = BadgeHandler(outf)
        xml.sax.parse("badges.xml", handler)
finally:
    stop_event.set()
