from api import wiki

WORDS = ["WIKIPEDIA"]

def sanitize_query(query):    
    upper_query = query.upper()
    sanitized_string = query
    idx = upper_query.find('WIKIPEDIA', 1)
    if(idx == -1):
        idx = len(upper_query)
    sanitized_string = upper_query[0:idx]
    return sanitized_string.replace("WIKIPEDIA","").strip()

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
    wiki_summary = wiki.search_wiki(sanitize_query(text))
    mic.say(wiki_summary.encode('ascii','ignore'))

def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    upperText = text.upper()
    return upperText.startswith('WIKI') or upperText.startswith('VIKI')
