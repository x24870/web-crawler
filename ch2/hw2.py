import requests, re
from bs4 import BeautifulSoup

def blog_post_count(url):
    soup = get_soup(url)
    if soup:
        return len(soup.find_all('div', 'card-blog'))


def img_crawler_count(url):
    soup = get_soup(url)
    if soup:
        imgs = soup.find_all('img', {'src': re.compile('crawler')})
        return len(imgs)

def lesson_count(url):
    soup = get_soup(url)
    if soup:
        rows = soup.find('table', 'table').tbody.find_all('tr')
        return len(rows)

def get_dcard_top10_title():
    url = 'https://www.dcard.tw/f'
    soup = get_soup(url)
    if soup:
        titles = soup.find_all('h3', re.compile('^PostEntry_title'))
        for i in range(10):
            print('{}. {}'.format(i+1, titles[i].text))

def get_soup(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup
        else:
            print("Status code abnormal, status code: {}".format(resp.status_code))
            return None
    except:
        print("Can't reach the website")
        return None


def main():
    url1 = 'http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html'
    url2 = 'http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html'
    print(blog_post_count(url1))
    print(img_crawler_count(url1))
    print(lesson_count(url2))
    get_dcard_top10_title()

if __name__ == '__main__':
    main()