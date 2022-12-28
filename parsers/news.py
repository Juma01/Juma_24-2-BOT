from pprint import pprint
import requests
from bs4 import BeautifulSoup


URL = "https://kaktus.media/?lable=8&date=2022-12-28&order=time"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
}


def get_html(url):
    reg = requests.get(url, headers=HEADERS)
    return reg


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all('div', class_="Tag--article")
    new = []
    for article in articles:
        article_title = {
            'title': article.find('a', class_="ArticleItem--name").string,
            'link': article.find('a', class_="ArticleItem--name").get('href'),
            'time': article.find('div', class_="ArticleItem--time").string,
        }
        new.append(article_title)
    return new


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        new = []
        for i in range(1, 2):
            html = get_html(f"{URL}/?lable=8&date=2022-12-2{i}&order=time")
            current_page = get_data(html.text)
            new.extend(current_page)
        return new
    else:
        raise Exception('Bad request in parsers!')


