import requests
import json

if __name__ == "__main__":
    # For a static page, General -> Request URL omit the parameters following the ?
    # For a dynamic content page using ajax query, use the requests filtered by XHR
    url = 'https://movie.douban.com/j/chart/top_list'

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
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    # General -> Request Method
    response = requests.get(url=url, params=param, headers=headers)

    # Response Headers -> Content-Type could be text(text) or json(json()), or binary graph(content)
    # check the sample response, it is enclosed by [] means it is a list
    list_json = response.json()

    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_json, fp=fp, ensure_ascii=False)

    # if Content-Type is text
    # page_text = response.text
    # with open('./insider.html', 'w', encoding='utf-8') as fp:
    #    fp.write(page_text)
    print('finish crawling!')