from scraper import Scraper

DOMAIN = 'https://azertag.az'


def get_article_urls(article_contents):
    try:
        articles = article_contents.find_all('h1', {'class': 'news-title'})
        for article in articles:
            for link in article.find_all('a'):
                full_link = DOMAIN + link.get('href')
                yield full_link

    except TypeError:
        print('something went wrong')


def get_articles_content(urls):
    for url in urls:
        a_sc = Scraper(url=url)
        a_content_bs = a_sc.scrape_article()
        a_content = a_content_bs.find('div', {'class': 'left-content'}).text

        yield a_content
