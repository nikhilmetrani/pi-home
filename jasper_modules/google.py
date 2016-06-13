from api import google 
import re

WORDS = ["GOOGLE", "SEARCH"]

def sanitize_query(query):
    upper_query = query.upper()
    sanitized_string = query
    idx = upper_query.find('GOOGLE', 1) 
    if(idx == -1):
        idx = len(upper_query)
    sanitized_string = upper_query[0:idx]
    str = sanitized_string.replace("GOOGLE","").replace("SEARCH","").strip()
    print str
    return str

def handle(text, mic, profile):
    """
	Responsible to do google search
    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    message = "Searching " 
    mic.say(message)
    searchQuery = sanitize_query(text)
    message = "Searching " + searchQuery
    mic.say(message)
    message = google.google(searchQuery) 
    mic.say(message)


def isValid(text):
    """
        Returns True if the text is related to the Google search.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bgoogle\b', text, re.IGNORECASE)) or bool(re.search(r'\bsearch\b', text, re.IGNORECASE)) 
