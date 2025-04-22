import requests

from models.news import News
from core.crawler import parser_news

def fetch_latest_news():
    url = 'https://zdnet.co.kr/news/?lstcode=0000&page=1'
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    raw_news = parser_news(response.text)
    return [News(**item) for item in raw_news]