import requests

api_url = 'https://wiki.biligame.com/blhx/api.php'

params = {
    'action': 'query',
    'titles': '分类:方案舰娘',
    "list": "categorymembers",
    'format': 'json'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0',
    'sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Microsoft Edge";v="152"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'gamecenter_wiki_UserName=409046849; gamecenter_wiki_UserGroups=bilibili; gamecenter_wiki__session=kmks02e6jonr0khmh5cadshkjm65s1m2; gamecenter_wiki_UserID=4627359; DedeUserID=409046849; DedeUserID__ckMd5=f1dd84d67ab6a654; SESSDATA=dcf126f5%2C1803647691%2C2f707%2A81CjBu6cDDfl2xXJhEEBIvpBae74Z4zzBpp8neEgctnQBWbNz5asRqJazUjEJf57OXkbUSVmxjcTNHaUFwQlJQU0NXN0dCaXJKeFE1OGY4azJNMXJrUTlPS1RPZWdvYjZqUEszcVp4aVNjLXRmQWRVLU1Tc0Jsbm5oNHBNWHhIOEFBOWEyMEhTcnFBIIEC; bili_jct=3e183e13273f9c6e08a72e335f80a431; sid=h10zc0ls; b_nut=1788260468; buvid3=0A0AFAF1-1CB6-2651-3293-8643748BD9E071534infoc; buvid_fp=62e3c199d296afddee17cf42cc39d37d; buvid4=0F039B47-1559-4021-3756-4E642B2F057C71803-026090119-lztCIumAysAxIuVLxHX1upnJgqZ7TO4iL/y2M+2lBAr9pd1oeSK4kii8lTkrkVUz; Hm_lvt_cb50e488eca598646f26b3bf09b83ada=1788260469,1788270269,1788333661; HMACCOUNT=2A8CDEF579ECC277; Hm_lpvt_cb50e488eca598646f26b3bf09b83ada=1788335267; b_lsid=F8C59AFB_1A06116D350',
}

response = requests.get(api_url, params=params, headers=headers)
print("响应码：", response.status_code)
response.encoding = 'utf-8'
print(response.text)

