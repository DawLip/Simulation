import sys, os
import time

from data import data

def debug():
    while True:
        if data['exit']:
            break

        print(data['id'])

        time.sleep(1)