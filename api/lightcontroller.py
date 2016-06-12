# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
# API module to switch room specific lights on or off
#

from Light import Light


class Room:
    Bedroom = 0
    Livingroom = 1
    Bathroom = 2
    Kitchen = 3


class LightState:
    off = 0
    on = 1

LIGHTS = [Light(Room.Bedroom), Light(Room.Livingroom), Light(Room.Bathroom), Light(Room.Kitchen)]
