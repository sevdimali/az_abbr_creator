import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape_article(self):
        req = requests.get(url=self.url)
        soup = BeautifulSoup(req.content, 'html.parser')
        return soup
