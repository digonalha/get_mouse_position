#!/usr/bin/env python3

from pynput.mouse import Button, Controller
import time
mouse = Controller()

def get_mouse_position():
    time.sleep(1)
    print('mouse position: {0}'.format(mouse.position))

get_mouse_position()
