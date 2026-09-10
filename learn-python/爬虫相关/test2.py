import requests
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Referer": "https://www.baidu.com/",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}


def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"{url}:请求失败")
        return None

def parse_one_page(html):
    pattern = re.compile(r'''<dd>.*?board-index.*?>(.*?)
                         </i>.*?title="(.*?)"
                         .*?主演：(.*?)''' + r'\n' +
                         r'.*?上映时间：(.*?)', re.S | re.X)
    items = re.findall(pattern, html)
    print(items)

def main():
    origin_url = 'https://www.maoyan.com/board/4?offset='
    urls = []
    ovie_information_list = []
    for x in range(0, 100, 10):
        urls.append(origin_url + str(x))

    print(urls)

    for url in urls:
        html = get_one_page(url)
        movie_information_list = parse_one_page(html)
        print(movie_information_list)


main()