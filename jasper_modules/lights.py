# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
# Jasper module to switch lights on or off
#
# Connections:
#    VCC:        2
#    Ground:     6
#    Relay switches -
#        Switch 0:    15 (GPIO 22)
#        Switch 1:    16 (GPIO 23)
#        Switch 2:    18 (GPIO 24)
#        Switch 3:    22 (GPIO 25)

import RPi.GPIO as GPIO
import sys
import random
import re
from client import jasperpath


class Relay:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pinList = [22,23,24,25]

    def switch(self, lamp, state):
        pin = self.pinList[lamp]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, (GPIO.HIGH if state == 0 else GPIO.LOW))
        print "Relay %s switched %s" % (lamp, ("off" if state == 0 else "on"))

WORDS = ["LIGHT", "LIGHTS", "ON", "OFF", "LAMP", "LAMPS"]

ROOM_RELAYS = {'bedroom': 0, 'kitchen': 1, 'livingroom': 2, 'bathroom': 3, 'all': 4}
LIGHT_STATES = {'off': 0, 'on': 1}


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by switching the specific light or all lights on or off.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    room = get_room(text)
    action = get_action(text)
    mic.say("switching " + room + " lights " + action)
    state = LIGHT_STATES[action]
    relay = Relay()
    if 'all' == room:
        rooms = list(ROOM_RELAYS.keys())
        for roomname in rooms:
            if 'all' != roomname:
                lamp = ROOM_RELAYS[roomname]
                relay.switch(lamp, state)
    else:
        lamp = ROOM_RELAYS[room]
        relay.switch(lamp, state)


def get_action(text):
    if bool(re.search(r'\bon\b', text, re.IGNORECASE)):
        return "on"
    if bool(re.search(r'\bof\b', text, re.IGNORECASE)):
        return "off"


def isValid(text):
    """
        Returns True if the input is related to light switching.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    keywords = ["light", "lights", "lamp", "lamps"]
    allwords = text.lower().split()
    for word in keywords:
        if word in allwords:
            return True
    return False


def get_room(text):
    words = text.lower().split()
    if "bedroom" in words:
        return "bedroom"
    if "bathroom" in words:
        return "bathroom"
    if "kitchen" in words:
        return "kitchen"
    if "living" in words:
        return "livingroom"
    if "livingroom" in words:
        return "livingroom"
    if "room" in words:
        return "livingroom"
    return "all"


def main():
    if len(sys.argv) > 2:
        [cmd,lamp,state] = sys.argv
        lamp = int(lamp)   # which lamp?
        state = int(state) # off/on?
        relay = Relay()
        relay.switch(lamp, state)
    else:
        print "Usage: %s <relay> <0/1>" % sys.argv[0]

if __name__ == "__main__":
    main()
