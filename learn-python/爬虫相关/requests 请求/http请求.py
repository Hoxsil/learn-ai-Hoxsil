import requests

response = requests.get("https://www.example.com")
print(f"这个是输出：{response.text}")