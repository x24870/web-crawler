import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
    print(get_elem_text(url, 'p'))
    print(get_elem_text(url, 'title'))
    print(get_elem_text(url, 'not_exist'))

def get_elem_text(url, elem):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(elem).text
    except:
        print('Can not reach the website or the element.')
        return None


if __name__ == '__main__':
    main()