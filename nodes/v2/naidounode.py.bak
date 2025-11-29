import requests
import datetime
import base64

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
    f"http://naidounode.cczzuu.top/node/{year}{MONTH}{DAY}-v2ray.txt"
]

# 发起请求并打印结果
for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        
        # 判断返回的数据是否为base64编码
        try:
            data = response.content
            data64 = base64.b64decode(data)
            data8 = data64.decode('utf-8')
            print(data8)
        except UnicodeDecodeError:
            print(response.text)  # 直接输出原始数据
        
    except requests.exceptions.RequestException as e:
        print(f"未获取到到节点，错误代码:{e}")
