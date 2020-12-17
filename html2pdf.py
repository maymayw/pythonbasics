import scrap_html_to_pdf as s
import requests
from lxml import etree

my_scrapper = s.Scrapper()

start_url = 'https://book.apeland.cn'
# Pack the request parameters
# Query String Parameters for a static page
# For a dynamic content page using ajax query, filter XHR
# could be in Form Data, then the data dictionary is used to set data parameter in the request
param = {
    'type': '17',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}

# UA fake pretend from a real browser
# inspect the webpage -> Network -> resend a request by refreshing
# pick the first request -> Headers -> Request Headers -> User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

# page = requests.get('https://reading.geek-docs.com/books/contagious-why-things-catch-on', params=param, headers=headers).text
# tree = etree.HTML(page)
# urls = tree.xpath('/html/body/section/div[1]/div/article/a/@href')
# for u in urls:
#     print(u)

# General -> Request Method
response = requests.get(url=start_url, params=param, headers=headers).text
tree = etree.HTML(response)
urls = tree.xpath('/html/body/div/div/div[1]/ul/li//li')

pages = {}
for u in urls:
    add = start_url + u.xpath('./a/@href')[0]
    title = u.xpath('./a//text()')[0].replace('\n', '').replace('\t', '').replace(' ', '')
    pages[title] = add
    my_scrapper.scrap(pages)