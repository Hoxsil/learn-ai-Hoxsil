import requests

API_URL = "https://minecraft.fandom.com/zh/api.php"

params = {
    "action": "query",
    "titles": "钻石",
    "prop": "extracts",
    "exintro": 1,       # 只取简介
    "format": "json",
    "formatversion": 2
}

headers = {
    "User‑Agent": "MyDemoApp/1.0 (your‑mail@example.com)"
}

resp = requests.get(API_URL, params=params, headers=headers)
data = resp.json()
print(resp.status_code)
page = data["query"]["pages"][0]
print(page["title"])
print(page["extract"])