from abbreviations import schwartz_hearst

from scraper import Scraper

URL = 'https://azertag.az/bolme/economy?page=13'
DOMAIN = 'https://azertag.az'
MAX_PAGE_COUNT = 5
sc = Scraper(url=URL)
content = sc.scrape_article()


def get_article_urls(article_contents):
    article_list = []
    try:
        articles = article_contents.find_all('h1', {'class': 'news-title'})
        for article in articles:
            for link in article.find_all('a'):
                article_list.append(DOMAIN + link.get('href'))

    except TypeError:
        articles = None

    return article_list


article_urls = get_article_urls(content)


def get_articles_content(urls):
    articles_content = []
    for url in urls:
        a_sc = Scraper(url=url)
        a_content_bs = a_sc.scrape_article()
        a_content = a_content_bs.find('div', {'class': 'left-content'}).text

        articles_content.append(a_content)
        return articles_content


texts = get_articles_content(article_urls)
abreviaturalar=[]
for text in texts:
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text=text, most_common_definition=True)
    abreviaturalar.append(pairs)

print(abreviaturalar)
