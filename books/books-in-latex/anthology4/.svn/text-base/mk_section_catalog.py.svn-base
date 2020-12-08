import os
import random

TEMPLATE = "\include{sections/%s}"

files = [ f for f in os.listdir("sections") if not os.path.isdir(f) ]

random.shuffle(files)

for f in files:
    base, ext = f.split(".")
    if ext == "tex":
        print TEMPLATE % base