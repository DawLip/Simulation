import time

from data import data
from app.UIComponents.section import Section

def debug():
    while not data['exit']:
        # print("#########################")
        # for s in Section.all: print(s.name)

        time.sleep(1)