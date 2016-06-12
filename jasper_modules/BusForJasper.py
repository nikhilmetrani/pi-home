# -*- coding: utf-8-*-
import re
from api.bustimings import BusTimings

WORDS = ["BUS", "TIMINGS" , "ARRIVAL", "TWENTY" , "NINE", "TWELVE" , "THIRTY EIGHT"]

bus = BusTimings()

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        Bus Timings.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    busInt = 0
    busStopId = 96129
    hasError = False
    response = 'Please contact administrator'

    try:

        lowerCaseText = text.lower()

        if "twenty" in lowerCaseText:
            busInt = 20
        elif "thirty eight" in lowerCaseText:
            busInt = 38
        elif "nine" in lowerCaseText:
            busInt = 9
        elif "twelve" in lowerCaseText:
            busInt = 12
        else:
            busInt = 0

        response = bus.getBusInformation(busStopId, busInt, 'Your')

    except Exception as e:
        hasError = True
        response = "ERROR %s" % e.message

    print("PSI Response : " + response)
    if hasError:
	    mic.say('You mentioned ' + text + ' which is not valid. Say Bus 20 or Bus 38')
    else:
	    mic.say(response)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """

    isValid = bool(re.search(r'\bBus\b', text, re.IGNORECASE))

    if not isValid:
        isValid = bool(re.search(r'\bTiming\b', text, re.IGNORECASE))

    if not isValid:
        isValid = bool(re.search(r'\bArrival\b', text, re.IGNORECASE))

    return isValid

