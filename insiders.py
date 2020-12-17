from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    url = 'https://dataroma.com/m/ins/ins.php'

    params = {
        't': 'd',
        'am': '0',
        'sym':'',
        'o': 'a',
        'd': 'd'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    page_text = requests.get(url, params=params, headers=headers).text

    soup = BeautifulSoup(page_text, 'lxml')

    print(soup.find('table',id="sum"))