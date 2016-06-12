from api import twitter 
import re

WORDS = ["TWEET", "TWITTER", "UPLOAD"]


def handle(text, mic, profile):
    """
    Responsible to upload image file to twitter 

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    message = "Uploading image to Twitter" 
    mic.say(message)
    lastImage = profile['latest_jpg']
    message = twitter.uploadToTwitter(lastImage, profile)
    mic.say(message)


def isValid(text):
    """
        Returns True if the text is related to the PSI.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\btweet\b', text, re.IGNORECASE)) or bool(re.search(r'\btwitter\b', text, re.IGNORECASE)) or bool(re.search(r'\bupload\b', text, re.IGNORECASE))
