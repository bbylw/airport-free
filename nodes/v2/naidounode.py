import requests
import datetime
import base64
import binascii

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

# 安全的Base64解码函数
def safe_base64_decode(data):
    """安全解码Base64数据，自动处理填充问题"""
    try:
        # 如果是bytes，转换为字符串
        if isinstance(data, bytes):
            data = data.decode('utf-8').strip()
        
        # 处理URL安全的Base64
        data = data.replace('-', '+').replace('_', '/')
        
        # 修复填充
        missing_padding = len(data) % 4
        if missing_padding != 0:
            data += '=' * (4 - missing_padding)
        
        # 解码
        decoded = base64.b64decode(data, validate=False)
        return decoded.decode('utf-8')
    except (binascii.Error, TypeError, UnicodeDecodeError) as e:
        print(f"Base64解码失败: {e}")
        return None

# 构建URL列表
urls = [
    f"http://naidounode.cczzuu.top/node/{year}{MONTH}{DAY}-v2ray.txt"
]

# 发起请求并打印结果
for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        
        # 尝试Base64解码
        decoded_data = safe_base64_decode(response.content)
        
        if decoded_data:
            print(decoded_data)
        else:
            # 如果解码失败，直接输出原始内容
            print(response.text)
        
    except requests.exceptions.RequestException as e:
        print(f"未获取到节点，错误代码: {e}")
