import bs4
import requests
from pprint import pprint


Keywords = ['дизайн, фото, web, python','IT']


HEADERS = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'Pragma': 'no-cache'

}


def find_keywords(url, keyword):
    resp = requests.get(url, headers=HEADERS)
    text = resp.text

    soup = bs4.BeautifulSoup(text, features="html.parser")

    def_articles = soup.find_all("article", class_='tm-article-presenter__content')

    for artic in def_articles:
        prevs = artic.find('div', class_="article-formatted-body")
        digest = prevs.text
        if keyword in digest:
            return 1
        else:
            return


base_url = "https://habr.com"
url = base_url + '/ru/all/'
resp = requests.get(url, headers=HEADERS)
text = resp.text


soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article", class_='tm-articles-list__item')

prevs_list = []
result_list = []

for artic in articles:
    date = artic.time.text
    title = artic.find('a', class_='tm-article-snippet__title-link')
    prevs = artic.find('div', class_="article-formatted-body")
    prevs_text = prevs.text

    href = base_url + title['href']
    span_title_text = title.span.text
    prevs_list.append([date, span_title_text, href, prevs_text])
    previews = [date, span_title_text, href, prevs_text]

    for i in Keywords:
        if i in previews[3]:
            result_list.append(f'Ключевое слово \"{i}\" найдено в preview. Название статьи => {span_title_text} / Дата статьи {date} / Ссылка {href}')
        if i in previews[1]:
            result_list.append(f'Ключевое слово \"{i}\" найдено в названии. Название статьи => {span_title_text} / Дата статьи {date} / Ссылка {href}')
        if find_keywords(previews[2], i) == 1:
            result_list.append(f'Ключевое слово \"{i}\" найдено в статье. Название статьи => {span_title_text} / Дата статьи {date} / Ссылка {href}')
pprint(result_list)





