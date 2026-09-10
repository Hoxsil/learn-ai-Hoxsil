import requests


url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win 64: x64) AppleWevKit/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("请求成功！")
else:
    print("请求失败，状态码：", response.status_code)

print(response.text)
