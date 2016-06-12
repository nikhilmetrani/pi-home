import requests
from itertools import * 

bing_api_key2 = 'f4ca2de03b6e421aa3df1cd882d17977'
category_business = 'Business'
category_science = 'ScienceAndTechnology'
category_entertainment = 'Entertainment'
category_polititcs = 'Politics'
category_world = 'World'
category_sports = 'Sports'
trending_news = 'trendingtopics'

def get_news_by_category(category, count = 5):
    headers = { u'Ocp-Apim-Subscription-Key': bing_api_key2, 'User-Agent' : 'Raspberry Pi' }
    params = { u'category' : category, 'mkt' : 'en-us',  }
    req = requests.get('https://bingapis.azure-api.net/api/v5/news/', params=params, headers=headers, )
    top5 = list(map(lambda x: x[u'name'], islice(req.json()[u'value'],count)))
    return top5

def get_business_news(count = 5):
    return get_news_by_category(category_business, count)

def get_science_news(count = 5):
    return get_news_by_category(category_science, count)

def get_entertainment_news(count = 5):
    return get_news_by_category(category_entertainment, count)

def get_politics_news(count = 5):
    return get_news_by_category(category_polititcs, count)

def get_world_news(count = 5):
    return get_news_by_category(category_world, count)

def get_sports_news(count = 5):
    return get_news_by_category(category_sports, count)

def get_all(count = 5):
    #all_news = [ get_world_news(2), get_politics_news(2), get_entertainment_news(1), get_sports_news(1) ]
    return get_news_by_category('',count)
