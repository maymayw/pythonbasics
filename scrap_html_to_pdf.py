import requests
from lxml import etree
import os
import os.path
import pdfkit
import re

class Scrapper:
    html_ext = '.html'
    pdf_ext = '.pdf'
    path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit_options = {'javascript-delay': '5000',
                      'no-stop-slow-scripts': '',
                      }

    def __init__(self, dest='C:/Users/may/Documents/booknotes/'):
        self.dest_dir = dest
        self.tailored_path = ()

    # using re to find matches need to be deleted in the page
    def set_tailor(self, paths):
        self.tailored_path = paths

    def save_tailored_pdffile(self, url, name):
        file_name = name + self.pdf_ext
        if not os.path.exists(self.dest_dir):
            os.makedirs(self.dest_dir)
        file_name = self.dest_dir + file_name
        if not os.path.exists(file_name):
            print("converting " + url + " to " + file_name)
            param = {
                'type': '17', 'interval_id': '100:90', 'action': '', 'start': '0', 'limit': '20'
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
            }

            page = requests.get(url, params=param, headers=headers).text
            new_page = page
            # with open('orig.html', 'w', encoding='utf-8') as f:
            #     f.write(new_page)
            # f.close()

            for p in self.tailored_path:
                # print(p)

                new_page = re.sub(p, '', page)

            with open('temp.html', 'w', encoding='utf-8') as f:
                f.write(new_page)
            f.close()
            try:
                pdfkit.from_url('./temp.html', file_name, options=self.pdfkit_options, configuration=self.pdfkit_config)
            except Exception as e:
                print(e)
                pass

    def save_pdffile(self, url, name):

        file_name = name + self.pdf_ext
        if not os.path.exists(self.dest_dir):
            os.makedirs(self.dest_dir)
        file_name = self.dest_dir + file_name
        if not os.path.exists(file_name):
            print("converting " + url + " to " + file_name)
            try:
                pdfkit.from_url(url, file_name, options=self.pdfkit_options, configuration=self.pdfkit_config)
            except Exception as e:
                print(e)
                pass

    # pages are dict of page names as keys and page urls as values
    # page names are pdf file names and urls are html pages to be saved as pdf file each
    def scrap(self, pages):

        total = len(pages)
        i = 1

        for k in pages:

            print(str(i) + '/' + str(total))
            #self.save_pdffile(pages[k], k)
            self.save_tailored_pdffile(pages[k], k)
            i += 1
