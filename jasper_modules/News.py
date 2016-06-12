from api import news
import re

WORDS = ["NEWS", "HEADLINES"]


def handle(text, mic, profile):
    """
    Responsible to read the News Headlines 

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    news_api = news.News()
    allNews = news_api.get_all()
    for newsStr in allNews:
        allNews += newsStr + " "
    mic.say(allNews)


def isValid(text):
    """
        Returns True if the text is related to the PSI.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bnews\b', text, re.IGNORECASE)) or bool(re.search(r'\bheadlines\b', text, re.IGNORECASE))
