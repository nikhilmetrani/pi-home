import requests
from itertools import *

bing_api_key2 = 'f4ca2de03b6e421aa3df1cd882d17977'
default_news_max_count = 3
default_news_max_headlines_count = 5
news_category_business = 'Business'
news_category_science = 'ScienceAndTechnology'
news_category_entertainment = 'Entertainment'
news_category_politics = 'Politics'
news_category_world = 'World'
news_category_sports = 'Sports'


class News:
    def __init__(self, profile=None):
        if profile is None:
            self.api_key = bing_api_key2
        else:
            self.api_key = profile["BING_API_KEY"]

    def get_news_by_category(self, category, max_count=None):
        headers = {u'Ocp-Apim-Subscription-Key': self.api_key, 'User-Agent': 'Raspberry Pi'}
        params = {
            u'category': category,
            u'mkt': 'en-us',
            u'freshness': 'Day'
        }
        if max_count is None:
            max_count = default_news_max_count
        if category != '':
            params[u'count'] = max_count
        else:
            params[u'headlineCount'] = max_count
        req = requests.get('https://bingapis.azure-api.net/api/v5/news/', params=params, headers=headers, )
        top = list(map(lambda x: x[u'name'], islice(req.json()[u'value'], max_count)))
        return top

    def get_business_news(self, max_count=None):
        return self.get_news_by_category(news_category_business, max_count)

    def get_science_news(self, max_count=None):
        return self.get_news_by_category(news_category_science, max_count)

    def get_entertainment_news(self, max_count=None):
        return self.get_news_by_category(news_category_entertainment, max_count)

    def get_politics_news(self, max_count=None):
        return self.get_news_by_category(news_category_politics, max_count)

    def get_world_news(self, max_count=None):
        return self.get_news_by_category(news_category_world, max_count)

    def get_sports_news(self, max_count=None):
        return self.get_news_by_category(news_category_sports, max_count)

    def get_all(self, max_count=default_news_max_headlines_count):
        return self.get_news_by_category('', max_count)
