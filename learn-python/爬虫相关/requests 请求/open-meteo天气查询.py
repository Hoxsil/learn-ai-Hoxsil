import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://open-meteo.com',
    'Referer': 'https://open-meteo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0',
    'sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Microsoft Edge";v="152"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    "latitude":"26.05942",
    "longitude":"119.198",
    "start_date":"2024-01-01",
    "end_date":"2024-12-31",
    "daily":"temperature_2m_mean,temperature_2m_max,temperature_2m_min,precipitation_sum,daylight_duration",
    "hourly":"temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,cloud_cover,wind_speed_10m,wind_direction_10m,is_day",
    "timezone":"Asia%2FTokyo",
    "format":"json",
    "timeformat":"unixtime",
}

url = 'https://archive-api.open-meteo.com/v1/archive'

response = requests.get(url, headers=headers, params=params)
