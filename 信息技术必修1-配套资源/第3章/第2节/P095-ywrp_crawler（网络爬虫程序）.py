import re
from urllib import request
from bs4 import BeautifulSoup

base_url = 'http://www.ywrp.gov.cn'

index_url = base_url + '/zjszyzlgb/'
index_page = request.urlopen(index_url)

index_soup = BeautifulSoup(index_page, 'html.parser')
index_list = index_soup.find('ul', attrs={'class': 'noborder'}).find_all('li')

article_items = []

for article_title in index_list:
    if not article_title.get('class') or 'split' not in article_title.get('class'):
        item = {
            'title': article_title.a.text,
            'link': article_title.a['href']
        }
        article_items.append(item)

for item in article_items:
    content_url = base_url + item['link']
    content_page = request.urlopen(content_url)
    content_soup = BeautifulSoup(content_page, 'html.parser')
    tables = content_soup.find('div', attrs={'class': 'conTxt'}).find_all('table')
    for table in tables:
        if table.find_previous_siblings():
            table_legend = table.previous_sibling.previous_sibling.text
        else:
            table_legend = table.parent.previous_sibling.previous_sibling.text

        table_legend = re.sub(r'\s+', '-', table_legend)

        file_name = item['title'] + '.' + table_legend + '.html'
        with open(file_name, 'w') as file:
            file.write(table.prettify())

