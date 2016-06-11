import wikipedia

WORDS = ["WIKIPEDIA"]

def search_wiki(query, sentences = 2):
    return wikipedia.summary(query, sentences = sentences)

def sanitize_query(query):    
    upper_query = query.upper()
    sanitized_string = query
    idx = upper_query.find('WIKIPEDIA', 1)
    if(idx == -1):
        idx = len(upper_query)
    sanitized_string = upper_query[0:idx]
    return sanitized_string

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
    wiki_summary = search_wiki(sanitize_query(text))
    mic.say(wiki_summary)

def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    upperText = text.upper()
    return upperText.startswith('WIKI') or upperText.startswith('VIKI')
