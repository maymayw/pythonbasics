import scrap_html_to_pdf as s
import requests
from lxml import etree
import re

my_scrapper = s.Scrapper(dest='C:/Users/may/Documents/leisure/tianguancifu/')

start_url = 'https://www.kunnu.com/tianguancifu'
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
urls = tree.xpath('/html/body/div/div/ul/li')
paths_to_drop = ('<div id="comments"[\S\s]*<!-- #comments -->',)
my_scrapper.set_tailor(paths_to_drop)

pages = {}
for u in urls:
    try:
        add = u.xpath('./a/@href')[0]
        title = u.xpath('./a//text()')[0].replace('\n', '').replace('\t', '').replace(' ', '')
    except IndexError:
        link = re.findall('http.*htm', u.xpath('./b/@onclick')[0])[0]
        add = link
        title = u.xpath('./b//text()')[0].replace('\n', '').replace('\t', '').replace(' ', '')
    finally:
        print(add + ' ' + title)
        pages[title] = add
# pages = {'引':'https://www.kunnu.com/meizhe/79400.htm',}
my_scrapper.scrap(pages)