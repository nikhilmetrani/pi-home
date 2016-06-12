# Copyright 2016 Nikhil Metrani
# Institute of Systems Science, National University of Singapore
# API module to switch lights on or off
#

import Relay as relctrl


class Light:
    def __init__(self, relay):
        self.relay = relay

    def switch(self, state):
        relctrl.switch(self.relay, state)

    def on(self):
        relctrl.switch(self.relay, 1)

    def off(self):
        relctrl.switch(self.relay, 0)

