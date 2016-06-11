from api import psireader 

WORDS = ["POLLUTION","NORTH","SOUTH","CENTRAL","WEST","EAST","ALL"]

def sanitize_query(query):    
    upper_query = query.upper()
    sanitized_string = query
    idx = upper_query.find('POLLUTION', 1)
    if(idx == -1):
        idx = len(upper_query)
    sanitized_string = upper_query[0:idx]
    return sanitized_string.replace("POLLUTION","").strip()

def handle(text, mic, profile):
    """
    Responsible to read the Singapore PSI value
    User can pronounce region directions to get the value    

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    psiReader = psireader.PSIReader()
    xmlValue = psiReader.getPSIUpdates()
    dict = {
        'NORTH': psireader.PSIReader.processXML(xmlValue, 'rNO', 'Singapore North'),
        'SOUTH': psireader.PSIReader.processXML(xmlValue, 'rSO', 'Singapore South'),
        'WEST': psireader.PSIReader.processXML(xmlValue, 'rWE', 'Singapore West'),
        'EAST': psireader.PSIReader.processXML(xmlValue, 'rEA', 'Singapore East'),
        'CENTRAL': psireader.PSIReader.processXML(xmlValue, 'rCE', 'Singapore Cenral')
    }	    
    searchDirection = sanitize_query(text)
    try:
	response = dict[searchDirection]
    except Exception as e:
        response = "ERROR"
    print("PSI Response : " + response)    
    if response == "ERROR":
	mic.say('You mentioned ' + searchDirection + ' which is not valid. Say north south east west or central')
    else:
	mic.say(response)

def isValid(text):
    """
        Returns True if the text is related to the PSI.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    upperText = text.upper()
    return upperText.startswith('POLLUTION')
