#!/usr/bin/python2.7

import panda as pd

tables = pd.read_html("www.chico.com/gasprices")

print(tables[0])
