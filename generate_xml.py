import datetime
import io
import string

import tqdm
import itertools
import fastrand

TARGET_SIZE = 1024 * 1024 * 1000

with tqdm.tqdm(total=TARGET_SIZE) as p:
    with io.StringIO() as f:
        print("""<?xml version="1.0" encoding="utf-8" ?>""", file=f)
        print("<badges>", file=f)
        for id in itertools.count():
            p.n = f.tell()
            p.update(n=0)
            if f.tell() >= TARGET_SIZE:
                break
            userid = fastrand.pcg32bounded(100000) + 1
            name = "".join(
                (string.ascii_lowercase)[
                    fastrand.pcg32bounded(len(string.ascii_lowercase))
                ]
                for x in range(5, 5 + fastrand.pcg32bounded(8))
            )
            date = datetime.datetime(2020, 1, 1) + datetime.timedelta(
                seconds=fastrand.pcg32bounded(86400 * 150)
            )
            cls = fastrand.pcg32bounded(10) + 1
            tagbased = fastrand.pcg32() & 1
            print(
                f'<row Id="{id}" UserId="{userid}" Name="{name}" Date="{date.isoformat()}" Class="{cls}" TagBased="{str(tagbased).title()}" />',
                file=f,
            )
        print("</badges>", file=f)
        with open("badges.xml", "w") as ff:
            ff.write(f.getvalue())
