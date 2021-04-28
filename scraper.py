import requests
from bs4 import BeautifulSoup


# url = 'https://bina.az/alqi-satqi/menziller?area_from=55&floor_first=false&has_bill_of_sale=true&items_view=list&price_from=65000&price_to=75000'
#
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# elanlar = soup.find_all('div', {'class': 'items-i'})
# # print(elanlar)
# for elan in elanlar:
#     info = elan.find('div',{'class':'card_params'})
#     infos = info.text
#     print(infos)
class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape_article(self):
        req = requests.get(url=self.url)
        soup = BeautifulSoup(req.content, 'html.parser')
        return soup
