from abbreviations import schwartz_hearst
from azertag import get_articles_content, get_article_urls
from scraper import Scraper

URL = 'https://azertag.az/bolme/economy?page=13'
MAX_PAGE_COUNT = 5
sc = Scraper(url=URL)
content = sc.scrape_article()

article_urls = get_article_urls(content)

texts = get_articles_content(article_urls)

for text in texts:
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text=text, most_common_definition=True)
    print(pairs)
