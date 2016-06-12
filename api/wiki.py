import wikipedia

def search_wiki(query, sentences = 2):
    return wikipedia.summary(query, sentences = sentences)
