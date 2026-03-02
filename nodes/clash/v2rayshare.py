import requests
import datetime

# 设置请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

# 获取当前日期
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

MONTH = f"{month:02d}"
DAY = f"{day:02d}"

# 构建URL列表
urls = [
    f"https://static.v2rayshare.net/{year}/{MONTH}/{year}{MONTH}{DAY}.yaml"
]

# 发起请求并打印结果
for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"未获取到到节点，错误代码：{e}")
