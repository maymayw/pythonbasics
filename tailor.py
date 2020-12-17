import scrap_html_to_pdf as s
import requests


my_scrapper = s.Scrapper()

start_url = 'https://book.apeland.cn/details/12/'

totail = ('/html/head', '/html/body/div/div/div[1]', '/html/body/div/div/div[2]/div[1]/div[1]', '/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/section/link', '/html/body/div/div/div/div/div[2]/i/div/div[2]/section/div/textarea',)
my_scrapper.set_tailor(totail)

my_scrapper.save_tailored_pdffile(start_url, 'test')