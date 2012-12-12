__author__ = 'makar'

import random

def gen2angle(gen):
    if gen=="D":
        angle=0
    elif gen=="r":
        angle=60
    elif gen=="R":
        angle=120
    elif gen=="B":
        angle=180
    elif gen=="L":
        angle=240
    elif gen=="l":
        angle=300
    else:
        angle=0

    return angle

def create_genom():
    _genom=""
    for i in range(1,6):
        _genom+=random.choice("DrRBLl")
    
    return _genom