import requests
import re
import time
import json


cookies = {
    'bid': 'Kosr_GEX3ps',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1788087710%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D',
    '_pk_id.100001.4cf6': '6feb7c16def23d2b.1788087710.',
    '_pk_ses.100001.4cf6': '1',
    '__utma': '30149280.1479252244.1785315574.1785668814.1788087710.3',
    '__utmb': '30149280.0.10.1788087710',
    '__utmc': '30149280',
    '__utmz': '30149280.1788087710.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utma': '223695111.1960571529.1788087710.1788087710.1788087710.1',
    '__utmb': '223695111.0.10.1788087710',
    '__utmc': '223695111',
    '__utmz': '223695111.1788087710.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'ap_v': '0,6.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Microsoft Edge";v="152"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0',
    # 'cookie': 'bid=Kosr_GEX3ps; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1788087710%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=6feb7c16def23d2b.1788087710.; _pk_ses.100001.4cf6=1; __utma=30149280.1479252244.1785315574.1785668814.1788087710.3; __utmb=30149280.0.10.1788087710; __utmc=30149280; __utmz=30149280.1788087710.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1960571529.1788087710.1788087710.1788087710.1; __utmb=223695111.0.10.1788087710; __utmc=223695111; __utmz=223695111.1788087710.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0',
}


def get_one_page(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print('请求失败！')
        return ''

def parse_one_page(html):
    pattern = re.compile(r'<em>(.*?)</em>.*?' +
                         r'<span class="title">(.*?)</span>.*?' +
                         r'导演: (.*?) .*?' +
                         r'主演: (.*?) .*?' +
                         r'<br>.*?(\d{3,4})&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\n', re.S)
    items = re.findall(pattern, html)
    return items

origin_url = 'https://movie.douban.com/top250?start='
urls = []
movie_information_list = []
for x in range(0, 250, 25):
    urls.append(origin_url + str(x) + '&filter=')

for url in urls:
    html = get_one_page(url)
    movie_information_list.extend(parse_one_page(html))
print(movie_information_list)
with open('豆瓣电影top250.txt', 'w', encoding='utf-8') as f:
    json.dump(movie_information_list, f, ensure_ascii=False, indent=2)
