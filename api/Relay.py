# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
# API to control relay switches
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

PIN_LIST = [22, 23, 24, 25]
RELAY_LIST = [0, 1, 2, 3]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def switch(relay, state):
    if relay in RELAY_LIST:
        pin = PIN_LIST[relay]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, (GPIO.HIGH if state == 0 else GPIO.LOW))
        print "Relay %s switched %s" % (relay, ("off" if state == 0 else "on"))
    else:
        print "Relay index " + relay + " is out of range. Valid values + " + RELAY_LIST