# -*- coding: utf-8-*-
import re
from api.weather import Weather
WORDS = ["WEATHER", "TODAY", "TOMORROW"]


def handle(text, mic, profile):
    """
    Responds to user-input, typically speech text, with a summary of
    the relevant weather for the requested date (typically, weather
    information will not be available for days beyond tomorrow).

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    weather_api = Weather()
    text = ''
    if text.upper().startswith("TOMORROW"):
        text = weather_api.get_tomo_text()
    else:
        text = weather_api.get_today_text()
    mic.say(text)


def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(weathers?|temperature|forecast|outside|hot|' +
                          r'cold|jacket|coat|rain)\b', text, re.IGNORECASE))
