# -*- coding: utf-8-*-
import random
import re
import picamera
from PIL import Image
import time
from time import strftime
import os

WORDS = ["CAMERA"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        Camera.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    dateTimeStr = strftime("%Y%m%d%H%M%S")
    fileName =  profile['pi_paths']['picam'] + dateTimeStr + ".jpg"
    latest_sym = profile['latest_jpg']
    camera = picamera.PiCamera()
    message = "Taking Pifie. Say  Cheese "
    mic.say(message)
    camera.capture(fileName)
    message = "Picture taken, saving  "
    mic.say(message)
    camera.close()

    image = Image.open(fileName)
    image.show()
    time.sleep(2)
    message = "You are looking fantastic today :)  "
    mic.say(message)
    time.sleep(1)
    image.close()
    if os.path.islink(latest_sym):
        os.unlink(latest_sym)
    os.symlink(fileName,latest_sym)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bCamera\b', text, re.IGNORECASE))

