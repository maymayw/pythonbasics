import requests
from lxml import etree
import os
import os.path
import pdfkit

root_dir = 'C:/Users/may/Documents/booknotes/'
html_ext = '.html'
pdf_ext = '.pdf'
dir = root_dir + 'deepinbook/'
path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
pdfkit_config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
pdfkit_options = {'javascript-delay': '10000',
                  'no-stop-slow-scripts': '',
                  }

def save_pdffile(url):
    parts = url.split('/')
    deep_dir = dir
    if url.endswith(html_ext):
        file_name = parts[-1]
        deep_dir += parts[-2] + '/'
    else:
        deep_dir += parts[-1] + '/'
        file_name = parts[-1] + html_ext
        url += '/' + file_name

    file_name = file_name.replace(html_ext, pdf_ext)
    if not os.path.exists(deep_dir):
        os.makedirs(deep_dir)
    file_name = deep_dir + file_name
    if not os.path.exists(file_name):
        print("converting " + url + " to " + file_name)
        try:
            pdfkit.from_url(url, file_name, options=pdfkit_options, configuration=pdfkit_config)
        except Exception:
            pass


if __name__ == '__main__':
    url = 'https://deepinbook.com/sitemap.xml'
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

    # General -> Request Method
    response = requests.get(url=url, params=param, headers=headers)

    with open('deep.txt', 'r') as f:
        fc = int(f.read())
    f.close()
    root = etree.fromstring(response.content)
    total = len(root)
    diff = total - fc

    if diff > 0:
        i = 1
        with open('deep.txt', 'w') as f:
            f.write(str(total))
        f.close()
        for u in root:
            if i <= diff:
                url = u[0].text
                print(str(i) + '/' + str(diff))
                save_pdffile(url)
            i += 1
