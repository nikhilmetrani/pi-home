import requests
from bs4 import BeautifulSoup


def google(query):
    params = {'nl': 'en', 'q': query.encode('utf8')}
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'}
    req = requests.get('https://www.google.com.sg/search', params=params, headers=headers)
    soup = BeautifulSoup(req.content, "lxml")
    span = soup.find('span', '_m3b')
    if span is None:
        span = soup.find('div', '_Oqb')
    if span is None:
        span = soup.find('div', '_sPg')
    if span is not None:
        result = span.text
    else:
        result = 'Could not find any results for it'
    return result


def main():
    print google("President of Singapore")
    print google("Prime minister of Singapore")
    print google("Distance between earth and sun")
    print google("Temperature of sun")
    print google("Temperature of Mars")
    print google("President of United States of America")


if __name__ == "__main__":
    main()
