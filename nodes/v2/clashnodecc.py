import requests
import datetime
import base64
import time

# 设置请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

# 设置超时时间（秒）
TIMEOUT = 10

# 获取当前日期
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

MONTH = f"{month:02d}"
DAY = f"{day:02d}"

def is_base64_encoded(data):
    """检查数据是否为有效的Base64编码"""
    try:
        decoded_data = base64.b64decode(data)
        encoded_data = base64.b64encode(decoded_data).decode('utf-8')
        original_str = data.decode('utf-8') if isinstance(data, bytes) else data
        return encoded_data.strip() == original_str.strip()
    except Exception:
        return False

def fetch_node_file(index):
    """获取指定索引的节点文件"""
    url = f"https://node.clashnode.cc/uploads/{year}/{MONTH}/{index}-{year}{MONTH}{DAY}.txt"
    
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        
        if response.status_code == 404:
            return None
            
        response.raise_for_status()
        
        data = response.content
        
        if is_base64_encoded(data):
            try:
                data64 = base64.b64decode(data)
                data8 = data64.decode('utf-8')
                return data8
            except UnicodeDecodeError:
                return response.text
        else:
            return response.text
            
    except requests.exceptions.RequestException:
        return None
    except Exception:
        return None

def main():
    index = 0
    consecutive_failures = 0
    max_consecutive_failures = 2
    
    while True:
        result = fetch_node_file(index)
        
        if result is None:
            consecutive_failures += 1
            if consecutive_failures >= max_consecutive_failures:
                break
        else:
            consecutive_failures = 0
            print(result)
        
        index += 1
        time.sleep(0.5)

if __name__ == "__main__":
    main()
