import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = 'http://reader.epubee.com/books/mobile/32/32d7a21f012c223e8e39d1e90e10b6db/'
    #http://reader.epubee.com/books/mobile/d3/d336727fffe29b23280225d0e4edd895/'
    #http://reader.epubee.com/books/mobile/32/32d7a21f012c223e8e39d1e90e10b6db/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    session = requests.Session()

    response = session.get(url, headers=headers)

    page = response.text
    save_page = True
    page_number = 1

    while save_page:
        #inner_content = BeautifulSoup(page, 'lxml').find('div', class_='readercontent-inner').prettify()
        #with open('book.html', 'a', encoding='iso-8859-1') as book:
        inner_content = BeautifulSoup(page, 'lxml').find('div', class_='readercontent-inner').prettify('iso-8859-1')
        with open('book.html', 'ab') as book:
            book.write(inner_content)
            print('next page', page_number)
        next_page_url = url + 'text{:05d}.html'.format(page_number)
        next_page = session.get(next_page_url, headers=headers)
        status = next_page.status_code
        print(next_page_url, status)
        if status == 200:
            page_number += 1
            page = next_page.text
        else:
            save_page = False

