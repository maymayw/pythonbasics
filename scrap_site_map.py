import requests
from lxml import etree
import os
import os.path
import pdfkit

root_dir = 'C:/Users/may/Documents/booknotes/'
path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
pdfkit_config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
pdfkit_options = {'javascript-delay': '10000',
                  'no-stop-slow-scripts': '',
                  }

def save_pdffile(url):
    parts = url.split('/')
    file_name = parts[-1].replace('html', 'pdf')
    dir = root_dir + parts[-2] + '/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    file_name = dir + file_name

    if not os.path.exists(file_name):
        print("converting" + file_name)
        try:
            pdfkit.from_url(url, file_name, options=pdfkit_options, configuration=pdfkit_config)
        except Exception:
            pass

# save_pdffile('https://reading.geek-docs.com/literature/zimmerman-telegram.html')

if __name__ == '__main__':
    url = 'https://reading.geek-docs.com/sitemap.xml'
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
    response = requests.get(url=url, params=param, headers=headers)

    with open('notes.txt', 'r') as f:
        fc = int(f.read())
    f.close()

    root = etree.fromstring(response.content)
    total = len(root)
    diff = total - fc

    if diff > 0:
        i = 1
        with open('notes.txt', 'w') as f:
            f.write(str(total))
        f.close()
        for u in root:
            if i <= diff:
                url = u[0].text
                print(str(i) + '/' + str(diff))
                if url.endswith('.html'):
                    save_pdffile(url)
                else:
                    page = requests.get(url, params=param, headers=headers).text
                    tree = etree.HTML(page)
                    urls = tree.xpath('/html/body/section/div[1]/div/article/a/@href')
                    for u in urls:
                        save_pdffile(u)
            i += 1